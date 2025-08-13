#Pip install opencv-contrib-python
#pip install mediapipe
#pip install cvzone
#pip install pyautogui
import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5, maxHands=2)
cap = cv2.VideoCapture(0)  # Use 0 for the default camera
cap.set(3, 600)
cap.set(4, 400)

while True:
    success, img = cap.read()

    if not success:
        print("Failed to capture frame")
        continue

    img = cv2.flip(img, 1)
    
    hands, img = detector.findHands(img)  # Detect hands
    if hands and hands[0]["type"] == "Left":
        fingers = detector.fingersUp(hands[0])
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        if totalFingers == 5:
            pyautogui.keyDown("right")
            pyautogui.keyUp("left")
        if totalFingers == 0:
            pyautogui.keyDown("left")
            pyautogui.keyUp("right")
            
    cv2.imshow('Camera Feed', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
