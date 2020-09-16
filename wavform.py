import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
# Import the wav files. It will be loaded in as a numpy array.
# sr represents the samplerate.
# Since we did not specify the samplerate when loading in the files,
# the default will be set to 22050.
guitar, sr = librosa.load('guitar.wav')
kick, sr = librosa.load('kick.wav')
snare, sr = librosa.load('snare.wav')
# Printing out shapes and samplerate.
print(f'Guitar Array: {guitar.shape}')
print(f'Kick Array: {kick.shape}')
print(f'Snare Array: {snare.shape}')
print(f'Samplerate: {sr}')
#Visualizing waveforms:
fig, ax = plt.subplots(1,3, figsize = (30,10), sharey = True)
librosa.display.waveplot(guitar, sr=sr, ax=ax[0])
ax[0].set(title = 'Guitar Waveform')
librosa.display.waveplot(kick, sr=sr, ax=ax[1])
ax[1].set(title = 'Kick Drum Waveform')
librosa.display.waveplot(snare, sr=sr, ax=ax[2])
ax[2].set(title = 'Snare Drum Waveform')
plt.show()
# Signal Envelope:
def env_mask(wav, threshold):
    # Absolute value
    wav = np.abs(wav)
    # Point wise mask determination.
    mask = wav > threshold
    return mask
# Initialize mask
g_mask = env_mask(guitar, sr, 0.005)
k_mask = env_mask(kick, sr, 0.005)
s_mask = env_mask(snare, sr, 0.005)
# Plotting the new signals
fig, ax = plt.subplots(1,3, figsize = (30,10), sharey = True)
# Visualize wave plots with mask applied.
librosa.display.waveplot(guitar[g_mask], sr=sr, ax=ax[0])
ax[0].set(title = 'Guitar Waveform')
librosa.display.waveplot(kick[k_mask], sr=sr, ax=ax[1])
ax[1].set(title = 'Kick Drum Waveform')
librosa.display.waveplot(snare[s_mask], sr=sr, ax=ax[2])
ax[2].set(title = 'Snare Drum Waveform')
plt.show()
