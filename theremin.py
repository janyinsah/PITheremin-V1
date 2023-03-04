# PI THEREMIN - 609IT END OF YEAR PROJECT
# CREATED BY JOSIAH ANYINSAH-BONDZIE
# STUDENT ID: 8624637

#---------------------------------------------------------------
# Modules needed for the creation of the PI Theremin.
import cv2
import mediapipe as mp
import uuid
import os
import numpy as np
from client import * 
#----------------------------------------------------------------
# Draw Hands -  Define Hand Solutions
mp_drawing = mp.solutions.drawing_utils # Drawing the hand landmarks (joints) to video on webcam.
mp_hands = mp.solutions.hands # Actual hand detection.
mp_drawing_styles = mp.solutions.drawing_styles # Style for hand detection.
#----------------------------------------------------------------
# Open up webcam and capture video by initialising each frame on cap
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame = camera.read()
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(5) and 'OxFF' == ord('q'):
        break
        camera.release()
        cv2.destroyAllWindows()
#----------------------------------------------------------------
# Apply hand landmark tracking.
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hand_detected = mp_hands.Hands(max_num_hands=2).process(frame)
#----------------------------------------------------------------
# Draw landmarks onto image.
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    if hand_detected.multi_hand_landmarks:
        for every_finger in hand_detected.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, every_finger, connections=mp_hands.HAND_CONNECTIONS)
            
#----------------------------------------------------------------
# Get hand landmark data.

#----------------------------------------------------------------
# Main Program, run.
#----------------------------------------------------------------

 