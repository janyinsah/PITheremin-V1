import numpy as np
import pyaudio
from scipy import signal

class AudioSamples: 
    #This is a class to define the sampling attributes for each wave generated for the PI Theremin. 
    s_rate = 44100 #Sampling Rate
    freq= 440.0 #Frequency (Hz)
    samples= 44100 #Number of samples
    x = np.arange(samples)

def gen_sine_wave(sine_y):
    
    #Generating the Sound Wave (Sine) for the PI Theremin.
    sine_y = 100*np.sin(2 * np.pi * AudioSamples.freq * AudioSamples.x / AudioSamples.s_rate)
    return sine_y
