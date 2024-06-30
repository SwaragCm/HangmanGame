import unittest
from unittest.mock import patch
from hangman import load_words, choose_word, print_word, load_hangman_parts, handle_guess, get_chances

class TestLoadWords(unittest.TestCase):
    def test_load_words(self):
        # Assuming dictionary.txt contains appropriate words
        words = load_words('dictionary.txt')
        self.assertIsInstance(words, list)
        for word in words:
            self.assertNotIn("'", word)

class TestChooseWord(unittest.TestCase):
    def setUp(self):
        self.words = ["hangman", "python", "programming"]

    def test_choose_word(self):
        word = choose_word(self.words)
        self.assertIn(word, self.words)

class TestPrintWord(unittest.TestCase):
    def setUp(self):
        self.word = "hangman"
        self.guessed_letters = ['h', 'a', 'n']

    def test_print_word(self):
        expected_output = 'h a n - - a n'
        self.assertEqual(print_word(self.word, self.guessed_letters), expected_output)

class TestHandleGuessSingleLetter(unittest.TestCase):
    def setUp(self):
        self.word = "hangman"
        self.guessed_letters = ['h', 'a', 'n']
        self.chances = 7
        self.hangman_parts = load_hangman_parts()

    def test_correct_guess(self):
        result, chances, hangman_part = handle_guess(self.word, self.guessed_letters, 'g', self.chances, self.hangman_parts)
        self.assertIn("Correct guess", result)

    def test_incorrect_guess(self):
        result, chances, hangman_part = handle_guess(self.word, self.guessed_letters, 'b', self.chances, self.hangman_parts)
        self.assertIn("Incorrect guess", result)

    def test_already_guessed(self):
        result, chances, hangman_part = handle_guess(self.word, self.guessed_letters, 'h', self.chances, self.hangman_parts)
        self.assertIn("already guessed", result)

    def test_out_of_chances(self):
        self.guessed_letters = []
        self.chances = 1
        result, chances, hangman_part = handle_guess(self.word, self.guessed_letters, 'b', self.chances, self.hangman_parts)
        self.assertIn("You ran out of chances", result)

class TestHandleGuessWholeWord(unittest.TestCase):
    def setUp(self):
        self.word = "hangman"
        self.guessed_letters = []
        self.chances = 7
        self.hangman_parts = load_hangman_parts()

    def test_correct_guess(self):
        result, chances, hangman_part = handle_guess(self.word, self.guessed_letters, 'hangman', self.chances, self.hangman_parts)
        self.assertIn("Congratulations", result)

    def test_incorrect_guess(self):
        result, chances, hangman_part = handle_guess(self.word, self.guessed_letters, 'program', self.chances, self.hangman_parts)
        self.assertIn("Incorrect guess", result)

class TestChancesLeft(unittest.TestCase):
    def setUp(self):
        self.chances = 7

    def test_chances_left(self):
        self.assertEqual(get_chances(self.chances), 7)
        self.chances -= 1
        self.assertEqual(get_chances(self.chances), 6)

if __name__ == "__main__":
    unittest.main()
