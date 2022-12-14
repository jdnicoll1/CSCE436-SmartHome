import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose 
pose = mpPose.Pose()

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                if(id == 13 or id == 14):
                    h, w, c = img.shape
                    print(id, lm)

        
    


        img_invert = cv2.flip(img, 1) #people are more used to inverted image
        
        cv2.imshow("Image", img_invert)
        if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
            break