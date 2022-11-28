import cv2
import time 
import os
import mediapipe as mp

#width and height of the video feed
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def detectHands(results): 
    
    
    if(results.multi_hand_landmarks): 
        for handLandmarks in results.multi_hand_landmarks: 
            return mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS)

def findPosition(results): 
    lmList = []
    if(results.multi_hand_landmarks): 
        myHand = results.multi_hand_landmarks[0]
        for id, lm in enumerate(myHand.landmark): 
            h,w,c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            #print(id, cx, cy)
            lmList.append([id,cx,cy])
            #cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)
    
    return lmList



if __name__ == "__main__": 

    while True:
        success, img = cap.read()
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        #continuously detect hands
        detectHands(results)
        landmarkList = findPosition(results)

        if(len(landmarkList) != 0): 
            if landmarkList[8][2] < landmarkList[6][2]:
                print("Index finger open")
    
        img_invert = cv2.flip(img, 1) #people are more used to inverted image
        cv2.imshow("Image", img_invert)
        if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
            break