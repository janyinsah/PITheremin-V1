import numpy as np
import pyaudio
from scipy import signal

def gen_sine_wave(sine_y):
    
    s_rate = 44100 #Sampling Rate
    freq= 440.0 #Frequency (Hz)
    samples= 44100 #Number of samples
    x = np.arange(samples)

    #Generating the Sound Wave (Sine) for the PI Theremin.
    sine_y = 100*np.sin(2 * np.pi * freq * x / s_rate)
    return sine_y

