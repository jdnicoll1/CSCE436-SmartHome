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
totalFingers = 0
function = ""

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
            #https://google.github.io/mediapipe/solutions/hands.html -- list of hand landmarks
            #if landmark 8 is below landmark 6, then finger is closed
            numFingers = []
            tipIds = [4,8,12,16,20]

            #thumb
            if(landmarkList[tipIds[0]][1] > landmarkList[tipIds[0]-1][1]):
                numFingers.append(1)
            else:
                numFingers.append(0)
            #not thumb
            for id in range(1, 5):
                if(landmarkList[tipIds[id]][2] < landmarkList[tipIds[id]-2][2]):
                    numFingers.append(1)
                else:
                    numFingers.append(0)

            totalFingers = numFingers.count(1) #count the number of fingers in the array to get number held up
            if(totalFingers == 1): 
                function = "Turn on TV"
            elif(totalFingers == 2): 
                function = "Volume Up"
            elif(totalFingers == 3): 
                function = "Volume Down"
            elif(totalFingers == 4): 
                function = "Turn on Oven"
            elif(totalFingers == 5): 
                function = "Turn on Car"
        else:
            totalFingers = 0
            function = ""

            
        #cv2.rectangle(img, (20,20), (280,150), (240,255,255))
        img_invert = cv2.flip(img, 1) #people are more used to inverted image
        #cv2.rectangle(img_invert, (20,250), (170,450), (240,255,255))
        cv2.putText(img_invert, str(totalFingers), (45,390), cv2.FONT_HERSHEY_PLAIN, 10, (255,255,0), 15)
        cv2.putText(img_invert, function, (375,70), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0), 2)
        
        cv2.imshow("Image", img_invert)
        if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
            break