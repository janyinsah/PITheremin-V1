#This generates a sine wave using mathematical functions and proceedures,
#Encapsualting them into a function to be called when generating samples.
                    #Created by Josiah Anyinsah-Bondzie
#---------------------------------------------------------
import numpy as np
import pyaudio
from scipy import signal
#---------------------------------------------------------
#Class defined to give attributes of of sound to create the sound wave.
class AudioSamples: 
    #This is a class to define the sampling attributes for each wave generated for the PI Theremin. 
    s_rate = 4800 #Sampling Rate
    freq= 440.0 #Frequency (Hz)
    samples= 48000 #Number of samples
    volume = 0.5 #Initial volume set volume
    duration = 1/freq #How long the sine wave will play.
    x = np.arange(samples)
#---------------------------------------------------------
#Function created to generate a sine wave using numpy, returns the value of the sine_way for teh audio stream.
def gen_sine_wave():
    #Generating the Sound Wave (Sine) for the PI Theremin.
    sine_y = 100*np.sin(2 * np.pi * AudioSamples.freq * AudioSamples.x / AudioSamples.s_rate)
    return sine_y 



