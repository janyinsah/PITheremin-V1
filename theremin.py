# PI THEREMIN - 609IT END OF YEAR PROJECT
# CREATED BY JOSIAH ANYINSAH-BONDZIE
# STUDENT ID: 8624637
#---------------------------------------------------------------
# Modules needed for the creation of the PI Theremin.
import cv2
import mediapipe as mp
import uuid
import os
import client
from psonic import *
import time
#----------------------------------------------------------------
# Draw Hands -  Define Hand Solutions
mp_drawing = mp.solutions.drawing_utils # Drawing the hand landmarks (joints) to video on webcam.
mp_hands = mp.solutions.hands # Actual hand detection.
mp_drawing_styles = mp.solutions.drawing_styles # Style for hand detection.
# Define OSC Client connection from client python library. 
set_server_parameter('127.0.0.1', 4560)
message = client.connect_to_client('127.0.0.1', 4560)
# Define Sine Wave attributes for python-sonic to send osc messages to.
frequency = 440
amplitude = 0.5 
duration = 5
#----------------------------------------------------------------
# Using psonic libraries to generate sine wave tone.
use_synth(SINE)
play(frequency, sustain=duration, amp=amplitude)
#----------------------------------------------------------------
# Open up webcam and capture video by initialising each frame on cap
while True:
    camera = cv2.VideoCapture(0)
    while camera.isOpened():
        ret, frame = camera.read()
        cv2.imshow('Hand Tracking', frame)

    # Apply hand tracking.
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        hand_detected = mp_hands.Hands(max_num_hands=2).process(frame)
#----------------------------------------------------------------
# Draw hands onto image (webcam).
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        if hand_detected.multi_hand_landmarks:
        # To get the first hand we index the landmarks at 0 as max_num_hands = 2 that means in the array of hands detected it must be 0 and 1.
            hand_landmark_items_first = hand_detected.multi_hand_landmarks[0]
            for every_landmark_item in hand_detected.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, every_landmark_item, connections=mp_hands.HAND_CONNECTIONS)

            left_hand_landmarks = hand_landmark_items_first if len(hand_detected.multi_hand_landmarks) >= 1 else None
            right_hand_landmarks = hand_detected.multi_hand_landmarks[1] if len(hand_detected.multi_hand_landmarks) >= 2 else None
#----------------------------------------------------------------
     # Get co-ordination point for both left hand and right hand.
            pitch = every_landmark_item.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * 100
            volume = every_landmark_item.landmark[mp_hands.HandLandmark.WRIST].x * 100
#----------------------------------------------------------------
            # Display handlandmark co-ordinations on opencv window.
            cv2.putText(frame, f'Pitch: {pitch} Hz', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, f'Volume: {volume:.2f}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
            # Send values of hand landmarks, to represent and change pitch and volume via osc messages.
            message.send_message("/osc/synth", ["pitch", pitch])
            message.send_message("/osc/synth", ["amp", volume])

            time.sleep(0.1)
    
    # This will display the hand landmark (joints) on the cv2 webcam window.
        cv2.imshow("Hand Tracking", frame)
    # Display current pitch, and volume values based on hand landmark input.
        if cv2.waitKey(5) and 'OxFF' == ord('q'):
            break
            camera.release()
            cv2.destroyAllWindows()
