#This module aims to generate a tone a different method, by sending messages through
#OSC Messages to Sonic Pi.
                #Created by Josiah Anyinsah-Bondzie
#---------------------------------------------------------
import time
from psonic import *
from client import *
from threading import Thread
import hands
#---------------------------------------------------------
#'post' sends the script message to the Sonic PI interface.
#This is done by asssinging the variable to the connect_to_client function
#Defined in client.py.
post = connect_to_client()
#----- ----------------------------------------------------
#Test to represent hand co-ordinates which will alter/change the pitch and amplitude of the wave.  
class hand_coords():
    hand_gesture_x = 10 #Frequency (Pitch    
    hand_gesture_y = 50 #Amplitude (Volume)
#---------------------------------------------------------
#Infinite loop which determines the length of time of which the sine wave will play.
def continous_tone(amp, vol, synth):
    
#---------------------------------------------------------






        