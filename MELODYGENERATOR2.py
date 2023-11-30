import wave
import struct
import math
import random

# Define the available notes and their corresponding MIDI numbers
notes = ["C", "D", "E", "F", "G", "A", "B"]
midi_numbers = [60, 62, 64, 65, 67, 69, 71]

# Define the melody structure
time_signature = 4  # Number of beats in a measure
melody_length = 8  # Number of notes in the melody

# Define the melodic patterns or motifs
patterns = [
    [0, 2, 4, 2],  # Example pattern 1
    [1, 3, 5, 3]   # Example pattern 2
]

# Generate a random melody
melody = []
for _ in range(melody_length):
    pattern = random.choice(patterns)
    note = random.choice(pattern)
    melody.append(note)

# Map the generated melody to MIDI notes
midi_melody = [midi_numbers[note] for note in melody]

# Set up the WAV file properties
sample_width = 2  # 2 bytes for 16-bit audio
frame_rate = 44100  # Sample rate
num_channels = 1  # Mono audio

# Create a WAV file and write the audio data
with wave.open("generated_melody.wav", "w") as wav_file:
    wav_file.setparams((num_channels, sample_width, frame_rate, 0, "NONE", "not compressed"))

    # Generate audio data for each MIDI note
    for note in midi_melody:
        frequency = 440 * (2 ** ((note - 69) / 12))  # Calculate the frequency of the note
        duration = 1  # Duration of each note in seconds

        # Generate audio samples for the note
        num_samples = int(frame_rate * duration)
        samples = [int(32767 * math.sin(2 * math.pi * frequency * t / frame_rate)) for t in range(num_samples)]

        # Pack the samples into binary data
        audio_data = struct.pack("<" + "h" * num_samples, *samples)

        # Write the audio data to the WAV file
        wav_file.writeframes(audio_data)

print("Melody exported as generated_melody.wav")