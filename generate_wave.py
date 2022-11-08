import numpy as np
import pyaudio
from scipy import signal

s_rate = 48000 #Sampling Rate
freq= 448 #Frequency (Hz)
samples = 48000 #Number of samples
x = np.arange(samples)

#Generating the Sound Wave (Sine) for the PI Theremin.
sine_y = 100*np.sin(2 * np.pi * freq * x / s_rate)


