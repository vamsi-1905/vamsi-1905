import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
width = 640
height = 480
cap.set(3, width)
cap.set(4, height)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    key = None

    for (x, y, w, h) in faces:
        center_x = x + w // 2
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.circle(frame, (center_x, y + h // 2), 5, (0, 255, 0), -1)

        if center_x < width//3:
            key = 'left'
        elif center_x > 2*width//3:
            key = 'right'
        else:
            key = 'up'
    
    if key:
        pyautogui.press(key)

    cv2.imshow("Head Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
