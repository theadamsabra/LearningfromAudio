import argparse
import librosa
import os
import numpy as np
from soundfile import write

description = '''
Create snippets of audio for Learning from Audio playground in the Jupyter Notebooks. Required arguments are the path to the audio file, the samplerate of the file,
and the number of seconds you want the snippet to be. It will save in the snippets folder, so do not delete it just because it is empty.
'''

# Create parser
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-p', '--path', help='Path to audio file to be sliced.', type=str, required=True)
parser.add_argument('-n', '--name', help='Name of snippet. Ideally, keep it to be the genre (rb, rap, rock, etc.) for ease of loading in later.', type=str, required=True)
parser.add_argument('-sr', help='Designate samplerate of audio file.', type=int, required=True)
parser.add_argument('-sec', help='Number of seconds the snippet is.', type=int, required=True)

# Get arguments
args = parser.parse_args()

# Check if snippets/ is exists. If it doesn't, create it.
if not os.path.isdir('snippets/'):
    os.mkdir('snippets/')

# Load in audio file and take random sample
song, _ = librosa.load(path = args.path, sr=args.sr) # Keeping mono=True meaning it is a vector.
# Take random point in the song. This will be the start point.
start_point = np.random.choice(song.shape[0])
# Now, add the amount of time to create snippet
end_point = start_point + args.sr * args.sec

# Save new file
write(file = f'snippets/{args.name}.wav', data=song[start_point:end_point], samplerate=args.sr)