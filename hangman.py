import random

def load_words(dictionary_file):
    with open(dictionary_file, 'r') as file:
        words = file.read().split()
    # Filter out words with apostrophes
    return [word for word in words if "'" not in word]

def load_hangman_parts():
    hangman_parts = [
        r"""
           +---+
               |
               |
               |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """
    ]
    return hangman_parts

def choose_word(words):
    return random.choice(words)

def print_word(word, guessed_letters):
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '- '
    return display_word.strip()

def handle_guess(word, guessed_letters, guess, chances, hangman_parts):
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            return "You've already guessed the letter '{}'. Try again.".format(guess), chances, None
        guessed_letters.append(guess)
        if guess not in word:
            chances -= 1
            if chances == 0:
                return "You ran out of chances. The word was '{}'.".format(word), chances, hangman_parts[-1]
            return "Incorrect guess. Chances left: {}.".format(chances), chances, hangman_parts[7 - chances]
        if all(letter in guessed_letters for letter in word):
            return "Congratulations! You guessed the word '{}'.".format(word), chances, None
        return "Correct guess. Word: {}".format(print_word(word, guessed_letters)), chances, None
    elif len(guess) == len(word) and guess.isalpha():
        if guess == word:
            return "Congratulations! You guessed the word '{}'.".format(word), chances, None
        else:
            chances -= 1
            if chances == 0:
                return "You ran out of chances. The word was '{}'.".format(word), chances, hangman_parts[-1]
            return "Incorrect guess. Chances left: {}.".format(chances), chances, hangman_parts[7 - chances]
    else:
        return "Invalid input. Please enter a single letter or guess the whole word.", chances, None



def get_chances(chances):
    return chances

def hangman_game(dictionary_file):
    words = load_words(dictionary_file)
    hangman_parts = load_hangman_parts()
    word = choose_word(words)
    
    guessed_letters = []
    chances = len(hangman_parts) - 1  # Start with maximum chances
    
    print("Welcome to Hangman!")
    print("Try to guess the word. You have {} chances.".format(chances))
    print(print_word(word, guessed_letters))
    
    while chances > 0:
        guess = input("Enter your guess : ").lower()
        result, chances, hangman_part = handle_guess(word, guessed_letters, guess, chances, hangman_parts)
        print(result)
        
        if hangman_part is not None:
            print(hangman_part)
        
        if "Congratulations" in result or "ran out of chances" in result:
            break
    
    print("The word was: {}".format(word))

if __name__ == '__main__':
    hangman_game('dictionary.txt')
