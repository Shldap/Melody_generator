import pygame
import random
from music21 import midi, stream, note, chord

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_SIZE = (800, 400)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Melody Generator")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define moods
MOODS = {
    "happy": [60, 62, 64, 65, 67, 69, 71, 72],
    "sad": [60, 62, 63, 65, 67, 68, 70, 72],
    "mysterious": [60, 61, 63, 66, 68, 69, 72, 74],
    "energetic": [60, 63, 65, 67, 70, 72, 75, 77]
}

# Set default mood
current_mood = "happy"

# Define constants
NUM_NOTES = 8
WAIT_TIME = 500


class Button:
    def __init__(self, mood, rect):
        self.mood = mood
        self.rect = rect

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def generate_melody(mood):
    """
    Generate a melody based on the selected mood using a Markov chain approach.
    """
    notes = MOODS[mood]
    transition_matrix = create_transition_matrix(notes)
    melody = generate_melody_with_markov_chain(transition_matrix, notes[0], NUM_NOTES)
    return melody


def create_transition_matrix(notes):
    """
    Create a transition matrix based on the given notes.
    """
    transition_matrix = {}
    for note in notes:
        transition_matrix[note] = {}

    for i in range(len(notes) - 1):
        current_note = notes[i]
        next_note = notes[i + 1]
        if next_note not in transition_matrix[current_note]:
            transition_matrix[current_note][next_note] = 0
        transition_matrix[current_note][next_note] += 1

    for current_note in transition_matrix:
        total_transitions = sum(transition_matrix[current_note].values())
        for next_note in transition_matrix[current_note]:
            transition_matrix[current_note][next_note] /= total_transitions

    return transition_matrix


def generate_melody_with_markov_chain(transition_matrix, start_note, length):
    """
    Generate a melody of the given length using a Markov chain approach.
    """
    melody = [start_note]
    current_note = start_note

    for _ in range(length - 1):
        if current_note not in transition_matrix:
            break

        choices = list(transition_matrix[current_note].keys())
        probabilities = list(transition_matrix[current_note].values())
        next_note = random.choices(choices, probabilities)[0]
        melody.append(next_note)
        current_note = next_note

    return melody


def play_melody(melody):
    """
    Play the melody using the chosen sound library.
    """
    # Create a MIDI stream
    melody_stream = stream.Stream()
    for note_value in melody:
        new_note = note.Note(note_value)
        melody_stream.append(new_note)

    # Save the MIDI file
    midi_file = midi.translate.streamToMidiFile(melody_stream)
    midi_file.open('output.mid', 'wb')
    midi_file.write()
    midi_file.close()

    # Load and play the MIDI file
    mf = midi.MidiFile()
    mf.open('output.mid')
    mf.read()
    mf.close()
    sp = midi.realtime.StreamPlayer(mf)
    sp.play()

def draw_buttons():
    """
    Draw the mood selection buttons on the window.
    """
    button_width = WINDOW_SIZE[0] // len(moods)

    for i, mood in enumerate(moods):
        button_rect = pygame.Rect(i * button_width, 0, button_width, 50)
        pygame.draw.rect(window, BLACK, button_rect)
        text = font.render(mood.capitalize(), True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        window.blit(text, text_rect)


def draw():
    """
    Draw the buttons on the window.
    """
    window.fill(WHITE)
    draw_buttons()
    pygame.display.update()


def main():
    """
    Main game loop.
    """
    global current_mood

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button_width = WINDOW_SIZE[0] // len(moods)
                    mood_index = mouse_pos[0] // button_width
                    current_mood = list(moods.keys())[mood_index]

        melody = generate_melody(current_mood)
        play_melody(melody)

        draw()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    # Load the piano sound file
    pygame.mixer.music.load("piano.wav")

    # Set up the font
    font_size = 24
    font = pygame.font.Font(None, font_size)

    main()
