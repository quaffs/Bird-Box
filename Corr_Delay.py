# Import Libraries 
import numpy as np 
from scipy.io.wavfile import read
from scipy import signal
import wave 

# Call in the WAV files 
original_audio = read('Cardinal Call 1_2.wav', 'rb')
recorded_audio = read('out_sine.wav', 'rb')

# Put the original wav file in the array
original_audio_array = np.array(original_audio[1])
original_audio_array = original_audio_array.flatten()

# Put the recorded wav file in the array
recorded_audio_array = np.array(recorded_audio[1])
recorded_audio_array = recorded_audio_array.flatten()

#Correlate the two arrays together 
corr = signal.correlate(recorded_audio_array, original_audio_array, 'full')

# get the delay time in milliseconds
delay = np.argmax(corr)

# Get the delay time in seconds
delay = (delay/1000)

# get the distance 
distance = delay / 44100 * 343 # sample_rate == 22050, m/s = speed of sound
print("Distance full: %.2f cm" % (distance * 100))