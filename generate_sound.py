### Main Program - Integrated & Created Modules ###
import time
import numpy as np
import pyaudio
import generate_wave

class generateSound:

    aud = pyaudio.PyAudio() #Define pyaudio product module

    class SoundAudio(generate_wave.AudioSamples):
        volume = 0.5 #Initial volume set volume
        duration = 5.0 #How long the sine wave will play.

    num_samples = int(generate_wave.AudioSamples.freq * SoundAudio.duration)
    samples = (SoundAudio.volume * generate_wave.gen_sine_wave().astype(np.float32))

#Convert to bytes
    output_bytes = (SoundAudio.volume * samples).tobytes()

#Create volume stream uplaod to pyaudio file format.
    stream = aud.open(format = pyaudio.paFloat32, channels = 1, rate = generate_wave.AudioSamples.s_rate, output = True)

    stream.write((SoundAudio.volume * samples).tobytes())


