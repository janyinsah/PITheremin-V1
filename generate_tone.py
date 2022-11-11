# Function which generates tone for the Pi Theremin.
from psonic import *
import pythonosc
from client import *

# Connect Script to Sonic PI.

clent_connect = client_attributes.client

create_client()

# Create function which generates a waveform tone for the PI Theremin.

def generate_sine_wave():
    sine_wave = False
    while True:
        if sine_wave:
            use_synth(SINE)
            sleep(0.25)
        else:
            continue 

