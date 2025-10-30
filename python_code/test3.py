import cv2
import mediapipe as mp
import pyautogui
import math

# --- Configuration ---
# Set the key for acceleration. A common choice is the 'up' arrow key.
ACCELERATE_KEY = 'up'
# Set the key for braking. Common choices are 'down' or 'space'.
BRAKE_KEY = 'down'
# Set the keys for steering.
LEFT_KEY = 'left'
RIGHT_KEY = 'right'
# Set the width of the central "dead zone" for steering as a percentage of screen width.
# A value of 0.25 means the middle 25% of the screen will not trigger a turn.
# This reduces steering sensitivity and makes it easier to go straight.
STEERING_DEAD_ZONE = 0.25


# --- Initialization ---
print("Initializing gesture controller...")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
# The main Hands class. We now configure it for two hands.
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Initialize PyAutoGUI for keyboard control
# Set a pause to prevent issues if the mouse moves to a corner.
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.0

# Initialize OpenCV to capture video from the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Get frame dimensions for calculating the dead zone
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame from webcam.")
    exit()
frame_height, frame_width, _ = frame.shape

# --- State Variables ---
# These variables track the current state of the keys to avoid redundant presses.
is_accelerating = False
is_braking = False
is_turning_left = False
is_turning_right = False

# --- Helper Function for Fist Detection ---
def is_fist(hand_landmarks):
    """
    Checks if a hand is in a fist gesture by verifying if the fingertips
    are curled below their respective middle joints.
    """
    landmarks = hand_landmarks.landmark
    # Check if the tip of each finger is below the PIP joint (second joint from base)
    is_curled = (
        landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
        landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
        landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y and
        landmarks[mp_hands.HandLandmark.PINKY_TIP].y > landmarks[mp_hands.HandLandmark.PINKY_PIP].y
    )
    return is_curled


print("Initialization complete. Starting gesture detection loop...")
print("\n--- CONTROLS ---")
print("Show your open hand(s) to the camera.")
print(f"  - ACCELERATE: Show one or two OPEN hands.")
print(f"  - BRAKE: Make a FIST with either hand.")
print(f"  - STEER: Move your open hand to the LEFT or RIGHT side of the screen.")
print(f"  - GO STRAIGHT: Keep your open hand in the CENTER.")
print("Press 'q' in the OpenCV window to quit.")


# --- Main Loop ---
while True:
    # 1. Read a frame from the webcam
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # 2. Process the Frame
    # Flip the image horizontally for a natural, mirror-like view
    img = cv2.flip(img, 1)
    # Convert the BGR image to RGB, as MediaPipe requires RGB input
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process the image and find hand landmarks
    results = hands.process(img_rgb)

    # Reset action flags for the current frame
    accelerate_action = False
    brake_action = False
    turn_left_action = False
    turn_right_action = False

    # 3. Gesture Recognition Logic
    if results.multi_hand_landmarks:
        # If any hand is detected, the default action is to accelerate.
        # This will be overridden if a brake gesture is detected.
        accelerate_action = True
        
        # Loop through all detected hands to check for gestures
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the image for visualization
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # --- BRAKE LOGIC (Highest Priority) ---
            if is_fist(hand_landmarks):
                brake_action = True
                # If braking, we cancel all other moves for this frame
                accelerate_action = False
                turn_left_action = False
                turn_right_action = False
                break # A single fist is enough to trigger a brake.
            
            # --- STEERING LOGIC (Position-Based) ---
            # Get the normalized x-coordinate of the wrist.
            wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
            
            # Define normalized boundaries for the dead zone
            left_bound = 0.5 - (STEERING_DEAD_ZONE / 2)
            right_bound = 0.5 + (STEERING_DEAD_ZONE / 2)

            # Check if hand is in the left or right steering zone
            # Note: We use two separate 'if' statements to allow detection
            # of two hands in opposite zones, which will cancel each other out.
            if wrist_x < left_bound:
                turn_left_action = True
            if wrist_x > right_bound:
                turn_right_action = True

    # If both turn signals are active (e.g., two hands on opposite sides), cancel them out to go straight.
    if turn_left_action and turn_right_action:
        turn_left_action = False
        turn_right_action = False

    # 4. Control the Game via Keyboard Simulation
    # Compare current action with the state to press/release keys only when needed.

    # Braking
    if brake_action and not is_braking:
        pyautogui.keyDown(BRAKE_KEY)
        is_braking = True
        print("Action: Brake [ON]")
    elif not brake_action and is_braking:
        pyautogui.keyUp(BRAKE_KEY)
        is_braking = False
        print("Action: Brake [OFF]")

    # Acceleration (only if not braking)
    if accelerate_action and not is_accelerating:
        pyautogui.keyDown(ACCELERATE_KEY)
        is_accelerating = True
        print("Action: Accelerate [ON]")
    elif not accelerate_action and is_accelerating:
        pyautogui.keyUp(ACCELERATE_KEY)
        is_accelerating = False
        print("Action: Accelerate [OFF]")

    # Turning Left (only if not braking)
    if turn_left_action and not is_turning_left:
        pyautogui.keyDown(LEFT_KEY)
        is_turning_left = True
        print("Action: Steer Left [ON]")
    elif not turn_left_action and is_turning_left:
        pyautogui.keyUp(LEFT_KEY)
        is_turning_left = False
        print("Action: Steer Left [OFF]")

    # Turning Right (only if not braking)
    if turn_right_action and not is_turning_right:
        pyautogui.keyDown(RIGHT_KEY)
        is_turning_right = True
        print("Action: Steer Right [ON]")
    elif not turn_right_action and is_turning_right:
        pyautogui.keyUp(RIGHT_KEY)
        is_turning_right = False
        print("Action: Steer Right [OFF]")


    # 5. Display the Output
    # Add a status display on the screen
    status_text = ""
    if is_turning_left: status_text += "LEFT "
    if is_turning_right: status_text += "RIGHT "
    if is_braking: status_text = "BRAKE"
    elif is_accelerating: status_text += "ACCELERATE"
    
    if not status_text: status_text = "NEUTRAL"
    
    # Draw the steering dead zone for visual feedback
    left_bound_px = int(frame_width * (0.5 - (STEERING_DEAD_ZONE / 2)))
    right_bound_px = int(frame_width * (0.5 + (STEERING_DEAD_ZONE / 2)))
    cv2.line(img, (left_bound_px, 0), (left_bound_px, frame_height), (0, 255, 255), 2)
    cv2.line(img, (right_bound_px, 0), (right_bound_px, frame_height), (0, 255, 255), 2)
    
    # Draw the status text
    cv2.putText(img, f'Action: {status_text}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Gesture Controller", img)

    # 6. Exit Condition
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
print("\nExiting program and releasing resources.")
# Release any held keys to prevent them from getting stuck
if is_accelerating: pyautogui.keyUp(ACCELERATE_KEY)
if is_braking: pyautogui.keyUp(BRAKE_KEY)
if is_turning_left: pyautogui.keyUp(LEFT_KEY)
if is_turning_right: pyautogui.keyUp(RIGHT_KEY)

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
hands.close()