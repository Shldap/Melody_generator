import pygame
import random

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
moods = {
    "happy": [60, 62, 64, 65, 67, 69, 71, 72],
    "sad": [60, 62, 63, 65, 67, 68, 70, 72],
    "mysterious": [60, 61, 63, 66, 68, 69, 72, 74],
    "energetic": [60, 63, 65, 67, 70, 72, 75, 77]
}

# Set default mood
current_mood = "happy"


def generate_melody(mood):
    """
    Generate a random melody based on the selected mood.
    """
    notes = moods[mood]
    melody = [random.choice(notes) for _ in range(8)]
    return melody


def play_melody(melody):
    """
    Play the generated melody using Pygame.
    """
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load(pygame.mixer.Sound("piano.wav"))
    pygame.mixer.music.play()

    for note in melody:
        pygame.mixer.music.set_pos(0.0)
        pygame.mixer.music.play(0, 0.0)
        pygame.time.wait(500)


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