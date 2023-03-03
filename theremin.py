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
#Draw Hands -  Define Hand Solutions
mp_drawing = mp.solutions.drawing_utils #Drawing the hand landmarks (joints) to video on webcam.
mp_hands = mp.solutions.hands #Actual hand detection.
#----------------------------------------------------------------



#Open up webcam and capture video by initialising each frame on cap
def callwebcam():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(10) and 'OxFF' == ord('q'):
            break
            cap.release()
            cv2.destroyAllWindows()
        

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = ''
    packets = connect_to_client(ip, port)
    packets.send_message()
    print(f"PI Theremin listening on IP: {ip} and port {port}")
    callwebcam()


 