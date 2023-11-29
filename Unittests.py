import unittest
from unittest.mock import patch
from music_generator import (
    generate_melody,
    create_transition_matrix,
    generate_melody_with_markov_chain,
)

class MusicGeneratorTests(unittest.TestCase):
    def test_generate_melody(self):
        # Test if a melody is generated
        melody = generate_melody("happy")
        self.assertTrue(len(melody) > 0)

    def test_create_transition_matrix(self):
        # Test if a transition matrix is created correctly
        notes = [60, 62, 64, 65, 67, 69, 71, 72]
        transition_matrix = create_transition_matrix(notes)
        self.assertEqual(len(transition_matrix), len(notes))

    def test_generate_melody_with_markov_chain(self):
        # Mock the random.choices function to always return the first choice
        with patch("random.choices") as mock_choices:
            mock_choices.return_value = [60]
            transition_matrix = {60: {62: 1.0}, 62: {64: 1.0}, 64: {65: 1.0}}
            melody = generate_melody_with_markov_chain(transition_matrix, 60, 3)
            self.assertEqual(len(melody), 3)
            self.assertEqual(melody, [60, 60, 60])

if __name__ == "__main__":
    unittest.main()
