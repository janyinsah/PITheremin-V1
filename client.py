#This creates a UPD client in which will allow python scripts to talk with the sonic pi client.
                    #Created by Josiah Anyinsah-Bondzie
#---------------------------------------------------------
                #OSC Client - Reusable
                #This file will be used for other future projects.
#---------------------------------------------------------
import argparse
import time
import random
#---------------------------------------------------------
from pythonosc import udp_client # Allows us to define sonic PI port and establish a connection locally via the loopback address.
#---------------------------------------------------------
#Created a method that returns ip and port to send a message to for the Sonic Pi DAW.
def connect_to_client(ip, port):
    send = udp_client.SimpleUDPClient(ip, port)
    return send
#---------------------------------------------------------


    
