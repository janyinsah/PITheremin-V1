#----------------------------------------------------------------
# Import Modues for the client file.
import argparse
import random
import time

from pythonosc import udp_client
from pythonosc import osc_message_builder
#----------------------------------------------------------------
# Function to connect supported 
def connect_to_client(ip, port):
    client = udp_client.SimpleUDPClient(ip, port)
    return client
