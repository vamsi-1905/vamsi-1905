import cv2
import mediapipe as mp
import pyautogui
import time

# --- Constants and Configuration ---
JUMP_THRESHOLD = 0.1
DUCK_THRESHOLD = 0.1
HORIZONTAL_THRESHOLD = 0.2
ACTION_COOLDOWN = 0.7
CALIBRATION_FRAMES = 60

# --- Initialization ---
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

# --- State Variables ---
player_state = "CALIBRATING"
last_action_time = 0
neutral_y = 0.5
neutral_y_levels = []

# --- Helper Functions ---
def perform_action(action):
    global last_action_time
    current_time = time.time()
    if current_time - last_action_time > ACTION_COOLDOWN:
        pyautogui.press(action)
        print(f"Action: {action.upper()} 🏃")
        last_action_time = current_time
        return True
    return False

# --- Main Loop ---
frame_count = 0
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    frame_height, frame_width, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]

        if all(lm.visibility > 0.5 for lm in [left_shoulder, right_shoulder]):
            shoulder_mid_x = (left_shoulder.x + right_shoulder.x) / 2
            shoulder_mid_y = (left_shoulder.y + right_shoulder.y) / 2

            if player_state == "CALIBRATING":
                cv2.putText(img, "CALIBRATING: Stand Still", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                if frame_count < CALIBRATION_FRAMES:
                    neutral_y_levels.append(shoulder_mid_y)
                    frame_count += 1
                else:
                    if neutral_y_levels:
                        neutral_y = sum(neutral_y_levels) / len(neutral_y_levels)
                    
                    # --- NEW: GRACE PERIOD COUNTDOWN ---
                    print("✅ Calibration Complete! Click on the game window NOW.")
                    for i in range(3, 0, -1):
                        # Display countdown on the OpenCV window
                        countdown_img = img.copy()
                        text = f"Click game! Starting in {i}..."
                        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 2, 3)[0]
                        text_x = (frame_width - text_size[0]) // 2
                        text_y = (frame_height + text_size[1]) // 2
                        cv2.putText(countdown_img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                        cv2.imshow("Subway Surfers AI Controller", countdown_img)
                        cv2.waitKey(1000) # Wait 1 second
                    
                    player_state = "NEUTRAL"
                    print("▶️ Controls Activated!")
                
                # We show the countdown image, but continue processing the original
                if player_state == "CALIBRATING": continue

            is_jumping = (neutral_y - shoulder_mid_y) > JUMP_THRESHOLD
            is_ducking = (shoulder_mid_y - neutral_y) > DUCK_THRESHOLD

            if shoulder_mid_x < (0.5 - HORIZONTAL_THRESHOLD):
                perform_action('left')
            elif shoulder_mid_x > (0.5 + HORIZONTAL_THRESHOLD):
                perform_action('right')

            if player_state == "NEUTRAL":
                if is_jumping:
                    if perform_action('up'):
                        player_state = "JUMPING"
                elif is_ducking:
                    if perform_action('down'):
                        player_state = "DUCKING"
            elif player_state == "JUMPING" and not is_jumping:
                player_state = "NEUTRAL"
            elif player_state == "DUCKING" and not is_ducking:
                player_state = "NEUTRAL"

            cv2.putText(img, f"STATE: {player_state}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            neutral_pixel_y = int(neutral_y * frame_height)
            jump_pixel_y = int((neutral_y - JUMP_THRESHOLD) * frame_height)
            duck_pixel_y = int((neutral_y + DUCK_THRESHOLD) * frame_height)
            
            cv2.line(img, (0, neutral_pixel_y), (frame_width, neutral_pixel_y), (0, 255, 0), 2)
            cv2.line(img, (0, jump_pixel_y), (frame_width, jump_pixel_y), (0, 0, 255), 2)
            cv2.line(img, (0, duck_pixel_y), (frame_width, duck_pixel_y), (255, 0, 0), 2)

    cv2.imshow("Subway Surfers AI Controller", img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()