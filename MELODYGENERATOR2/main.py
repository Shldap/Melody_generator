
import math
import tkinter as tk
from tkinter import messagebox
import wave
import struct
import random

# Define the available notes and their corresponding MIDI numbers
notes = ["C", "D", "E", "F", "G", "A", "B"]
midi_numbers = [60, 62, 64, 65, 67, 69, 71]

# Define the melodic patterns or motifs for each mood
patterns = {
    "happy": [
        [0, 2, 4, 2],  # Pattern 1
        [1, 3, 5, 3]  # Pattern 2
    ],
    "sad": [
        [3, 1, 0, 2],  # Pattern 1
        [5, 3, 2, 4]  # Pattern 2
    ],
    "calm": [
        [0, 1, 2, 1],  # Pattern 1
        [3, 4, 5, 4]  # Pattern 2
    ]
}


# Melody generator function
def generate_melody():
    mood = mood_selection.get()
    selected_patterns = patterns[mood]

    # Generate a random melody
    melody = []
    for _ in range(melody_length.get()):
        pattern = random.choice(selected_patterns)
        note = random.choice(pattern)
        melody.append(note)

    # Map the generated melody to MIDI notes
    midi_melody = [midi_numbers[note] for note in melody]

    # Generate audio data
    audio_data = generate_audio_data(midi_melody)

    # Export the melody as a WAV file
    export_melody(audio_data, mood)


# Generate audio data for the given MIDI notes
def generate_audio_data(midi_notes):
    frame_rate = 44100  # Sample rate
    duration = 1  # Duration of each note in seconds

    samples = []
    for note in midi_notes:
        frequency = 440 * (2 ** ((note - 69) / 12))  # Calculate the frequency of the note

        # Generate audio samples for the note
        num_samples = int(frame_rate * duration)
        note_samples = [int(32767 * math.sin(2 * math.pi * frequency * t / frame_rate)) for t in range(num_samples)]
        samples.extend(note_samples)

    # Pack the samples into binary data
    audio_data = struct.pack("<" + "h" * len(samples), *samples)
    return audio_data


# Export the melody as a WAV file
# Export the melody as a WAV file
def export_melody(audio_data, mood):
    sample_width = 2  # 2 bytes for 16-bit audio
    num_channels = 1  # Mono audio
    sample_rate = 44100  # Sample rate (frames per second)

    # Create a WAV file and write the audio data
    try:
        with wave.open(f"generated_melody_{mood}.wav", "wb") as wav_file:
            wav_file.setnchannels(num_channels)
            wav_file.setsampwidth(sample_width)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(audio_data)
        messagebox.showinfo("Success", f"Melody exported as generated_melody_{mood}.wav")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the GUI
window = tk.Tk()
window.title("Melody Generator")

# Melody length label and entry field
melody_length_label = tk.Label(window, text="Melody Length:")
melody_length_label.pack()
melody_length = tk.IntVar(value=8)
melody_length_entry = tk.Entry(window, textvariable=melody_length)
melody_length_entry.pack()

# Mood selection dropdown
mood_label = tk.Label(window, text="Select Mood:")
mood_label.pack()
moods = ["happy", "sad", "calm"]
mood_selection = tk.StringVar(value="happy")
mood_dropdown = tk.OptionMenu(window, mood_selection, *moods)
mood_dropdown.pack()

# Generate button
generate_button = tk.Button(window, text="Generate Melody", command=generate_melody)
generate_button.pack()

# Run the GUI
window.mainloop()
print("Melody exported as generated_melody.wav")

        # Write the audio data to the WAV file
        wav_file.writeframes(audio_data)

print("Melody exported as generated_melody.wav")
