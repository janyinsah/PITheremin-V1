import cv2 #openc library for video input
import mediapipe as mp #import the framework that allows for hand detection

#Hand tracking objects & nodes for hand modeling functionality
#It will be easier to use these instead of calling the path everytime it needs to be used.

class track_hands:

    draw_my_hands = mp.solutions.drawing_utils
    class_of_hands = mp.solutions.hands
    webcam = cv2.VideoCapture(0)

    framewidth = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
    frameheight = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)

#Access the video provided by the camera (webcam).


#Instantiating a class of hands to be detected through each stream.
    with class_of_hands.Hands(static_image_mode = False, min_detection_confidence = 0.7, min_tracking_confidence = 0.7, max_num_hands=2) as hands:
        while True:
            ret, frame = webcam.read() #Returns tuple from the videocapture object, to check if the frames are read correctly.
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) #Converts the RGB format to BGR to be read by OpenCV through the process method.


            if results.multi_hand_landmarks != None: #If hands are detected across each frame
                for hand_landmarks in results.multi_hand_landmarks: #For each landmark in the total of hand mark items
                    draw_my_hands.draw_landmarks(frame, hand_landmarks, class_of_hands.HAND_CONNECTIONS) #Calls the drawing utils method defined above using draw my hands 
                    #then labels them across each node in each hand landmark from the class of hands method

            if cv2.waitKey(1) == 27: #Frame remains open untill a esc is pressed.
                break

    cv2.destroyAllWindows() # destroy all windows after the while loop is broken.
    webcam.release() # camera is released and no longer being used.



    