# Function which generates tone for the Pi Theremin.
from psonic import *
import pythonosc
from client import *

# Connect Script to Sonic PI.

parcel = call_client()


# Create function which generates a waveform tone for the PI Theremin.

while True:
    note = play(70)
    parcel.send_message('/play_tone', note)
    print(note)
    sleep(1)




        

