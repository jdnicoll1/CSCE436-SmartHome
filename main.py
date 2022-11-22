import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if(results.multi_hand_landmarks): 
        for handLandmarks in results.multi_hand_landmarks: 
            mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS)

    img_invert = cv2.flip(img, 1) #people are more used to inverted image
    cv2.imshow("Image", img_invert)

    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
        break