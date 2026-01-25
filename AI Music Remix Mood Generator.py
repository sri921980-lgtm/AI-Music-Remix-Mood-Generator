# ===============================
# AI Music Remix Mood Generator
# Complete Colab-ready Python Code
# ===============================

# Step 1: Install required libraries (run only once)
!pip install librosa numpy soundfile pydub

# -------------------------------
# Step 2: Import libraries
import librosa
import numpy as np
import soundfile as sf
from IPython.display import Audio
from google.colab import files
import os

# -------------------------------
# Step 3: Upload your original audio file
print("Upload your original music file (.wav or .mp3)")
uploaded = files.upload()  # Upload one file

# Get uploaded file name
input_audio = list(uploaded.keys())[0]

print(f"Uploaded file: {input_audio}")

# -------------------------------
# Step 4: Define remix function
def remix_audio(input_file, mood, output_file):
    """
    Generate mood-based music remix
    moods: Happy, Sad, Calm, Energetic
    """
    y, sr = librosa.load(input_file, sr=None)

    # Mood parameters
    if mood == "Happy":
        rate = 1.2
        pitch = 2
    elif mood == "Sad":
        rate = 0.8
        pitch = -2
    elif mood == "Calm":
        rate = 0.9
        pitch = 0
    elif mood == "Energetic":
        rate = 1.3
        pitch = 3
    else:
        rate = 1.0
        pitch = 0

    # Apply tempo and pitch changes
    y = librosa.effects.time_stretch(y, rate=rate)
    y = librosa.effects.pitch_shift(y, sr=sr, n_steps=pitch)

    # Save output
    sf.write(output_file, y, sr)
    return output_file

# -------------------------------
# Step 5: Generate remixes for all moods
moods = ["Happy", "Sad", "Calm", "Energetic"]
output_files = []

for mood in moods:
    out_file = f"remixed_{mood}.wav"
    remix_audio(input_audio, mood, out_file)
    output_files.append(out_file)
    print(f"Generated {mood} remix: {out_file}")

# -------------------------------
# Step 6: Play original and remixed audios
print("\nOriginal Audio:")
Audio(input_audio)

for mood, file in zip(moods, output_files):
    print(f"\n{mood} Remix Audio:")
    display(Audio(file))  # display() shows audio player in Colab

# -------------------------------
# Step 7: Optional - Download remixed files
from google.colab import files
for file in output_files:
    files.download(file)
