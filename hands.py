#----------------------------------------------------------------
#Import Modues
import cv2
import mediapipe as mp
import uuid
import os
import numpy as np
#----------------------------------------------------------------
#Draw Hands -  Define Hand Solutions
mp_drawing = mp.solutions.drawing_utils #Drawing the hand landmarks (joints) to video on webcam.
mp_hands = mp.solutions.hands #Actual hand detection.
#----------------------------------------------------------------
#Open up webcam and capture video by initialising each frame on cap.
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(10) and 'OxFF' == ord('q'):
        break
        cap.release()
        cv2.destroyAllWindows()

 