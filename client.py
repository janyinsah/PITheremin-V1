#This creates a UPD client in which will allow python scripts to talk with the sonic pi client.

import time
import random

from pythonosc import udp_client

class client_attributes:
    client = udp_client.SimpleUDPClient('127.0.0.1', 4559)

def create_client():
    while True:
        client_attributes.send_message("/bpm", random.randint(40,200))
        time.sleep(5)



    
