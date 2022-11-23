#This method will generate a sound wave using the attributes and functions generated in generate_wave.py
                #Created by Josiah Anyinsah-Bondzie
#---------------------------------------------------------
import time
import numpy as np
import pyaudio
import generate_wave as gw
from scipy import signal
#---------------------------------------------------------
#Function declared to generate sound when called over x(duration) period of time.
def play_sound(): #Declaring the sound as a function. 
    #We may be able to later add parameters for frequency and amplitudfe which will represent the each landmark on the mediapipe hands solution.

    aud = pyaudio.PyAudio() #Define pyaudio product module

    num_samples = int(gw.AudioSamples.freq * gw.AudioSamples.duration)
    samples = (gw.AudioSamples.volume * gw.gen_sine_wave().astype(np.float32))

#Convert to bytes
    output_bytes = (gw.AudioSamples.volume * samples).tobytes()

#Create volume stream uplaod to pyaudio file format.
    stream = aud.open(format = pyaudio.paFloat32, channels = 1, rate = gw.AudioSamples.s_rate, output = True)

    stream.write((gw.AudioSamples.volume * samples).tobytes())
#---------------------------------------------------------
#Function is called to playback sound.
play_sound()
