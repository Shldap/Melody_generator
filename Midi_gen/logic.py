import pretty_midi
import random

def generate_midi(source_midi):
    # Load the source MIDI file
    midi_data = pretty_midi.PrettyMIDI(source_midi)

    # Create a transition matrix to represent the Markov chain
    transition_matrix = {}

    # Iterate over all the drum notes in the MIDI data
    for instrument in midi_data.instruments:
        if not instrument.is_drum:
            continue
        for note in instrument.notes:
            if note.pitch not in transition_matrix:
                transition_matrix[note.pitch] = {}
            next_pitch = note.pitch + 1
            if next_pitch not in transition_matrix[note.pitch]:
                transition_matrix[note.pitch][next_pitch] = 0
            transition_matrix[note.pitch][next_pitch] += 1

    # Choose a random starting pitch
    pitch = random.choice(list(transition_matrix.keys()))

    # Generate a sequence of pitches using the Markov chain
    sequence = []
    for _ in range(16):
        sequence.append(pitch)
        if pitch in transition_matrix:
            next_pitches = list(transition_matrix[pitch].keys())
            probabilities = [transition_matrix[pitch][next_pitch] for next_pitch in next_pitches]
            pitch = random.choices(next_pitches, weights=probabilities)[0]
        else:
            pitch = random.choice(list(transition_matrix.keys()))

    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI()

    # Create a drum instrument
    drum_program = pretty_midi.instrument_name_to_program('Acoustic Bass Drum')
    drum_track = pretty_midi.Instrument(program=drum_program)

    # Add drum notes to the drum track
    for pitch in sequence:
        start_time = len(drum_track.notes) * 0.25
        end_time = start_time + 0.25
        drum_note = pretty_midi.Note(
            velocity=100,
            pitch=pitch,
            start=start_time,
            end=end_time
        )
        drum_track.notes.append(drum_note)

    # Add the drum track to the MIDI data
    midi_data.instruments.append(drum_track)

    return midi_data
