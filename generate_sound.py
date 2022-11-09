### Main Program - Integrated & Created Modules ###
import time
import numpy as np
import pyaudio
import generate_wave
from scipy import signal

def play_sound(): #Declaring the sound as a function. 
    #We may be able to later add parameters for frequency and amplitudfe which will represent the each landmark on the mediapipe hands solution.

    aud = pyaudio.PyAudio() #Define pyaudio product module

    num_samples = int(generate_wave.AudioSamples.freq * generate_wave.AudioSamples.duration)
    samples = (generate_wave.AudioSamples.volume * generate_wave.gen_sine_wave().astype(np.float32))

#Convert to bytes
    output_bytes = (generate_wave.AudioSamples.volume * samples).tobytes()

#Create volume stream uplaod to pyaudio file format.
    stream = aud.open(format = pyaudio.paFloat32, channels = 1, rate = generate_wave.AudioSamples.s_rate, output = True)

    stream.write((generate_wave.AudioSamples.volume * samples).tobytes())


play_sound()
