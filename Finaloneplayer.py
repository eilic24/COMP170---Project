# COMP 170 Final Project
# Assignment: Hang In There! Hangman Project - Single Player Mode
# Name and Loyola ID/email: Ela Ilic (00001662221) and Emujin Otgonbayar (00001767505)
# Date: November 24, 2026
#
# DESCRIPTION:
# Select a single-player secret word and run a console Hangman round (round function is also reused by two-player mode)
#
# QUESTIONS:
# None
#
# PROBLEM ANALYSIS & KEY ISSUES:
# A repeated or invalid guess must not use an attempt, so guesses must be validated before updating the round.
#
# PROGRAM PSEUDOCODE:
# When single_player is called: get the secret word using get_word and pass the secret word to play.
# When play is called by either mode create an empty guess history and set mistakes to zero, and while fewer than six mistakes have been made and no win exists: display the current round, get a valid new guess and record the guess, then apply the letter/whole word guessing rule. Finally, reveal the final word and display the result.
#
# FUNCTIONS:
# valid_word: Check whether text contains only lowercase letters
# read_words: Load words from a text file
# normal_words: Obtain a word from the random-word package
# get_word: Select a secret word for the chosen difficulty
# single_player: Coordinate a single-player round
# guess: Obtain a valid new guess
# display: Display the current round
# check_win: Determine whether the word has been solved
# play: Play/go through one Hangman round

import random

max_mistakes = 6

#ASCII Drawings Used
hangman = [
    r"""
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
        """
]


def valid_word(word: str) -> bool:
        """Determine whether text is a nonempty lowercase alphabetic word.
        Parameters: word: the text to check
        Preconditions: word is a string.
        Returns True if every character is a lowercase letter a-z and the string is not empty; otherwise False.
        Postconditions: The original text is unchanged.
        Steps: If the word is empty, return False, examine each character and if a character is outside a-z, return False. Return True after all characters pass.
        """
        if len(word) == 0:
                return False
        for letter in word:
                if letter not in "qwertyuiopasdfghjklzxcvbnm":
                        return False
        return True


def read_words(filename: str) -> list[str]:
        """Load the lines of a word-list file.
        Parameters: filename: the name or location of the text file.
        Preconditions: The file exists and is readable.
        Returns a list containing the file's lines without line endings.
        Postconditions: The file is closed after reading.
        Steps: open the file, read its contents and separate them into lines, close the file. Return the list.
        """
        with open(filename) as file:
                words = file.read().splitlines()
        return words


def normal_words() -> str:
        """Get a secret word from the random-word package.
        Parameters None
        Preconditions: The random-word package is installed and its generator successfully supplies a lowercase word.
        Returns the generated word.
        Postconditions: A generated word has been returned.
        Steps: Import RandomWords and create a word generator. Request and return one random word.
        """
        from random_word import RandomWords
        generate = RandomWords()
        return generate.get_random_word()

def get_word(difficulty: str) -> str:
        """Select a secret word for the chosen difficulty.
        Parameters:difficulty: Either "easy" or "hard".
        Preconditions: For easy mode, easy_words.txt is readable and contains at least one valid lowercase word. For hard mode, normal_words can supply a valid word.
        Returns the selected secret word.
        Postconditions: A word has been selected for the round.
        Steps: If the difficulty is easy: Load easy_words.txt using read_words and randomly select and return one listed word. Otherwise: Return a word from normal_words.
        """
        if difficulty == "easy":
                words = read_words("easy_words.txt")
                return random.choice(words)
        else:
                return normal_words()


def single_player(difficulty: str) -> None:
        """Go through one single-player round.
        Parameters: difficulty: Either "easy" or "hard".
        Preconditions: The selected word source is available.
        Returns None.
        Postconditions: One single-player round has finished.
        Steps: Obtain a secret word using get_word and call play with that word.
        """
        secret_word = get_word(difficulty)
        play(secret_word)


def guess(guessed_letters: list[str]) -> str:
        """Get a valid guess that has not already been made.
        Parameters: guessed_letters: previously accepted letter and word guesses.
        Preconditions: The player user inputs into console input.
        Returns a nonempty lowercase a-z guess absent from the history.
        Postconditions: The guess history is unchanged.
        Steps: ask for a letter or whole-word guess. While the guess is invalid or already recorded: explain the input problem and ask again. Return the valid new guess.
        """
        user_guess = input("Guess a letter or the whole word: ")
        while not valid_word(user_guess) or user_guess in guessed_letters:
                if not valid_word(user_guess):
                        print("Enter letters a-z only")
                else:
                        print("You have already guessed that. Try again")
                user_guess = input("Guess a letter or the whole word: ")
        return user_guess

def display(secret_word: str, guessed_letters: list[str], mistakes: int, reveal_word: bool = False) -> None:
        """Display the current state of a Hangman round.
        Parameters: secret_word: the lowercase word being guessed,
                guessed_letters: previously accepted letter and word guesses,
                mistakes: the number of mistakes, from zero through six,
                reveal_word: whether to show every letter
        Preconditions: mistakes is a valid index in the drawing list.
        Returns None
        Postconditions: The round state has been printed without changes to the secret word, history, or mistake count.
        Steps: display the drawing for the mistake count and build the displayed word one character at a time. Show a letter if guessed or if reveal_word is true. Otherwise, show an underscore. Display the word, guess history, and remaining attempts.
        """
        print(hangman[mistakes])
        shown_word = ""
        for letter in secret_word:
                if letter in guessed_letters or reveal_word:
                        shown_word += letter + " "
                else:
                        shown_word += "_ "
        print("Word:", shown_word)
        if len(guessed_letters) == 0:
                print("Previous guesses: none")
        else:
                print("Previous guesses:", end = " ")
                for previous_guess in guessed_letters:
                        print(previous_guess, end = " ")
                print()
        print("Remaining guesses: ", max_mistakes - mistakes)


def check_win(secret_word: str, guessed_letters: list[str]) -> bool:
        """Determine whether the secret word has been solved.
        Parameters: secret_word: the nonempty lowercase word being guessed,
                guessed_letters: previously accepted letter and word guesses.
        Preconditions: The secret word contains only letters a-z.
        Returns: true if the whole word or all its letters were guessed; otherwise False.
        Postconditions: The word and guess history are unchanged.
        Steps: If the whole word is in the history, return True. Examine each letter in the secret word and if any letter is absent from the history, return False. Return True when every letter has been guessed.
        """
        if secret_word in guessed_letters:
                return True
        for letter in secret_word:
                if letter not in guessed_letters:
                        return False
        return True

def play(secret_word: str) -> None:
        """Coordinate one Hangman round.
        Parameters: secret_word: the nonempty lowercase word to be guessed
        Preconditions: The word contains only letters a-z.
        Returns None
        Postconditions: The round has ended with a win or loss, and the final word and result have been displayed.
        Steps: create an empty guess history and set mistakes to zero. While mistakes are below the limit and the word is unsolved: display the current round and obtain and record a valid new guess. If the guess has one letter: report whether the letter is in the word and add one mistake if it is absent. Otherwise: report whether the whole word is correct and set mistakes to the limit if the word is incorrect. Display the final round with the word revealed and display a win or loss message.
        """
        guessed_letters: list[str] = []
        mistakes = 0
        while mistakes < max_mistakes and not check_win(secret_word, guessed_letters):
                display(secret_word, guessed_letters, mistakes)
                user_guess = guess(guessed_letters)
                guessed_letters.append(user_guess)
                if len(user_guess) == 1:
                        if user_guess in secret_word:
                                print("Correct letter!")
                        else:
                                print("Incorrect letter!")
                                mistakes += 1
                else:
                        if user_guess == secret_word:
                                print("Correct word!")
                        else:
                                print("Incorrect word! You lose!")
                                mistakes = max_mistakes
        display(secret_word, guessed_letters, mistakes, reveal_word = True)
        if check_win(secret_word, guessed_letters):
                print("You win!")
        else:
                print("You lose! The word was: ", secret_word)
