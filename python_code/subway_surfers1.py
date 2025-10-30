import cv2
import mediapipe as mp
import pyautogui
import time
import numpy as np

# --- GPU Configuration ---
# Check for CUDA support
print("[INFO] Checking GPU availability...")
print(f"OpenCV CUDA support: {cv2.cuda.getCudaEnabledDeviceCount() > 0}")

# Force MediaPipe to use GPU if available
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Use first GPU

# --- Constants and Configuration ---
JUMP_THRESHOLD = 0.1
DUCK_THRESHOLD = 0.1
HORIZONTAL_THRESHOLD = 0.2
ACTION_COOLDOWN = 0.7
CALIBRATION_FRAMES = 60

# --- GPU-Accelerated Initialization ---
mp_pose = mp.solutions.pose
# Enable GPU acceleration for MediaPipe
pose = mp_pose.Pose(
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5,
    model_complexity=2,  # Higher complexity for better GPU utilization
    enable_segmentation=False,  # Disable segmentation to save GPU memory
    smooth_landmarks=True
)
mp_draw = mp.solutions.drawing_utils

# Initialize camera with GPU-friendly settings
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Cannot open camera")
    exit()

# Set camera properties for optimal GPU processing
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Reduce buffer to minimize latency

# --- GPU Memory Objects ---
gpu_frame = None
gpu_frame_rgb = None

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
        print(f"Action: {action.upper()}")
        last_action_time = current_time
        return True
    return False

def gpu_flip_frame(frame):
    """Flip frame using GPU acceleration if available"""
    try:
        if cv2.cuda.getCudaEnabledDeviceCount() > 0:
            gpu_frame = cv2.cuda_GpuMat()
            gpu_frame.upload(frame)
            gpu_flipped = cv2.cuda.flip(gpu_frame, 1)
            result = gpu_flipped.download()
            return result
        else:
            return cv2.flip(frame, 1)
    except:
        return cv2.flip(frame, 1)

def gpu_color_convert(frame):
    """Convert color space using GPU acceleration if available"""
    try:
        if cv2.cuda.getCudaEnabledDeviceCount() > 0:
            gpu_frame = cv2.cuda_GpuMat()
            gpu_frame.upload(frame)
            gpu_rgb = cv2.cuda.cvtColor(gpu_frame, cv2.COLOR_BGR2RGB)
            result = gpu_rgb.download()
            return result
        else:
            return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    except:
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# --- Main Loop ---
frame_count = 0
print("[INFO] Starting GPU-accelerated processing...")

# Warm up GPU
if cv2.cuda.getCudaEnabledDeviceCount() > 0:
    print("[INFO] Warming up GPU...")
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    for _ in range(5):
        gpu_flip_frame(dummy_frame)
        gpu_color_convert(dummy_frame)
    print("[SUCCESS] GPU warmed up!")
else:
    print("[INFO] No GPU detected, using CPU processing")

while True:
    success, img = cap.read()
    if not success:
        break

    # GPU-accelerated image processing
    img = gpu_flip_frame(img)
    frame_height, frame_width, _ = img.shape
    img_rgb = gpu_color_convert(img)
    
    # MediaPipe processing (automatically uses GPU if available)
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
                cv2.putText(img, f"GPU Mode: {cv2.cuda.getCudaEnabledDeviceCount() > 0}", (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                
                if frame_count < CALIBRATION_FRAMES:
                    neutral_y_levels.append(shoulder_mid_y)
                    frame_count += 1
                    # Show progress bar
                    progress = frame_count / CALIBRATION_FRAMES
                    cv2.rectangle(img, (50, 130), (50 + int(300 * progress), 150), (0, 255, 0), -1)
                    cv2.rectangle(img, (50, 130), (350, 150), (255, 255, 255), 2)
                else:
                    if neutral_y_levels:
                        neutral_y = sum(neutral_y_levels) / len(neutral_y_levels)
                    
                    # --- Grace period countdown ---
                    print("[SUCCESS] Calibration Complete! Click on the game window NOW.")
                    for i in range(3, 0, -1):
                        countdown_img = img.copy()
                        text = f"Click game! Starting in {i}..."
                        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 2, 3)[0]
                        text_x = (frame_width - text_size[0]) // 2
                        text_y = (frame_height + text_size[1]) // 2
                        cv2.putText(countdown_img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                        cv2.imshow("GPU Subway Surfers Controller", countdown_img)
                        cv2.waitKey(1000)
                    
                    player_state = "NEUTRAL"
                    print("[INFO] GPU Controls Activated!")
                
                if player_state == "CALIBRATING": 
                    continue

            # Movement detection
            is_jumping = (neutral_y - shoulder_mid_y) > JUMP_THRESHOLD
            is_ducking = (shoulder_mid_y - neutral_y) > DUCK_THRESHOLD

            # Horizontal movement
            if shoulder_mid_x < (0.5 - HORIZONTAL_THRESHOLD):
                perform_action('left')
            elif shoulder_mid_x > (0.5 + HORIZONTAL_THRESHOLD):
                perform_action('right')

            # Vertical movement state machine
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

            # Draw UI elements
            cv2.putText(img, f"STATE: {player_state}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.putText(img, f"GPU: {'ON' if cv2.cuda.getCudaEnabledDeviceCount() > 0 else 'OFF'}", (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0) if cv2.cuda.getCudaEnabledDeviceCount() > 0 else (0, 0, 255), 2)
            
            # Draw threshold lines
            neutral_pixel_y = int(neutral_y * frame_height)
            jump_pixel_y = int((neutral_y - JUMP_THRESHOLD) * frame_height)
            duck_pixel_y = int((neutral_y + DUCK_THRESHOLD) * frame_height)
            
            cv2.line(img, (0, neutral_pixel_y), (frame_width, neutral_pixel_y), (0, 255, 0), 2)
            cv2.line(img, (0, jump_pixel_y), (frame_width, jump_pixel_y), (0, 0, 255), 2)
            cv2.line(img, (0, duck_pixel_y), (frame_width, duck_pixel_y), (255, 0, 0), 2)

    cv2.imshow("GPU Subway Surfers Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Reduced wait time for better GPU performance
        break

cap.release()
cv2.destroyAllWindows()
print("[INFO] GPU processing complete!")