#This creates a UPD client in which will allow python scripts to talk with the sonic pi client.

import argparse
import time
import random

from pythonosc import udp_client

class client_attributes: #Determine the address and port UDP mssages will operate on. 
    client = udp_client.SimpleUDPClient('127.0.0.1', 4559)

def create_client():
    while True:
        client_attributes.client.send_message("/bpm", 120)
        time.sleep(5)





    
