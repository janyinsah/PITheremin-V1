#This creates a UPD client in which will allow python scripts to talk with the sonic pi client.
#---------------------------------------------------------
import argparse
import time
import random
#---------------------------------------------------------
from pythonosc import udp_client # Allows us to define sonic PI port and establish a connection locally via the loopback address.
#---------------------------------------------------------
#Defined a class which holds server details. (Experimenting with OOP. This isn't needed at all.)
class server_details:
    ip = '127.0.0.1'
    port = 4560
#---------------------------------------------------------
#Created a method that returns ip and port to send a message to for the Sonic Pi DAW.
def connect_to_client():
    send = udp_client.SimpleUDPClient(server_details.ip, server_details.port)
    return send
#---------------------------------------------------------


    
