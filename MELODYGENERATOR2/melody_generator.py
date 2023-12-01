import math
import wave
import struct
import random

# Define the available notes and their corresponding MIDI numbers
notes = ["C", "D", "E", "F", "G", "A", "B"]
midi_numbers = [60, 62, 64, 65, 67, 69, 71]

# Define the melodic patterns or motifs for each mood and genre
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
    ],
    "rnb": [
        [0, 4, 3, 2],  # Pattern 1
        [1, 5, 4, 3]  # Pattern 2
    ],
    "drill": [
        [2, 1, 3, 0],  # Pattern 1
        [4, 3, 5, 2]  # Pattern 2
    ],
    "hip-hop": [
        [0, 1, 2, 3],  # Pattern 1
        [4, 3, 2, 1]  # Pattern 2
    ]
}

# Define the chord progressions for different genres
chord_progressions = {
    "rnb": [
        [0, 4, 7],  # Chord 1 (C Major)
        [5, 9, 12],  # Chord 2 (F Major)
        [3, 7, 10],  # Chord 3 (A Minor)
        [4, 8, 11]  # Chord 4 (Bb Major)
    ],
    "drill": [
        [0, 3, 7],  # Chord 1 (C Major)
        [2, 5, 9],  # Chord 2 (D Minor)
        [4, 7, 11],  # Chord 3 (E Minor)
        [1, 5, 8]  # Chord 4 (G Major)
    ],
    "hip-hop": [
        [0, 4, 7],  # Chord 1 (C Major)
        [2, 5, 9],  # Chord 2 (D Minor)
        [4, 7, 11],  # Chord 3 (E Minor)
        [1, 5, 8]  # Chord 4 (G Major)
    ],
    "metro_boomin": [
        [0, 3, 7],  # Chord 1 (C Major)
        [2, 5, 8],  # Chord 2 (D Minor)
        [3, 6, 9],  # Chord 3 (E Minor)
        [1, 4, 8]  # Chord 4 (G Major)
    ]
}


# Melody generator function
def generate_melody():
    mood = mood_selection.get()
    selected_patterns = patterns[mood]
    selected_chord_progression = chord_progressions[mood]

    melody_length = melody_length_entry.get()
    try:
        melody_length = int(melody_length)
    except ValueError:
        messagebox.showerror("Error", "Invalid melody length")
        return

    melody = []

    # Generate melody notes
    for _ in range(melody_length):
        pattern = random.choice(selected_patterns)
        note_index = random.choice(pattern)
        melody.append(notes[note_index])

    # Generate chord progression
    chord_progression = []
    for chord in selected_chord_progression:
        chord_notes = [notes[note_index] for note_index in chord]
        chord_progression.append(chord_notes)

    # Print the generated melody and chord progression
    print("Melody:", melody)
    print("Chord Progression:", chord_progression)
