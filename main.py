# PI Theremin main program.
import numpy
import hands as hand
import client 
from psonic import *

# Functions
def hand_amplitude(**arggs):
    pass


def hand_volume(**arggs):
    pass

def check_hand_in_raneg(x, y):
    pass

def create_axis(x, y):
    pass


# Main Program Running

if __name__ == "__main__":
    packets = client.connect_to_client('127.0.0.1', '4557')
    while True:
    # Define current pitch. 
        pitch = 75
        packets.send_message('/play_this', pitch)
        sleep(0.5)

