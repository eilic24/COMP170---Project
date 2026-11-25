# COMP 170 Final Project - Multiplayer
# Assignment: Hang In There! Hangman Project
# Name and Loyola ID/email: Ela Ilic (00001662221) and Emujin Otgonbayar (00001767505)
# Date: November 24, 2026
#
# DESCRIPTION:
# Player 1 supplies a secret word for player 2 to guess.The shared Hangman round handles player 2's guesses.
#
# QUESTIONS:
# None
#
# PROBLEM ANALYSIS & KEY ISSUES:
# Player 2 should not see player 1's secret word during entry,so the word is requested through getpass.
#
# PROGRAM PSEUDOCODE:
# When two_player is called: get a valid secret word using word_to_guess. Then tell player 2 to begin guessing and call the shared play function with the secret word.
#
# FUNCTIONS:
# valid_word: Check whether the proposed secret word is valid
# word_to_guess: Obtain a valid secret word from player 1
# two_player: Coordinate one two-player round


from getpass import getpass
from one_player import play

def valid_word(word: str) -> bool:
        """Determine whether text is a nonempty lowercase alphabetic word.
        Parameters: word: the proposed secret word.
        Preconditions: word is a string.
        Returns True if the word is nonempty and contains only a-z; otherwise False.
        Postconditions: The original word is unchanged.
        Steps: set validity according to whether the word is nonempty and examine each character. Mark the word invalid if any character is outside a-z. Return the validity result.
        """
        valid = len(word) > 0
        for letter in word:
                if letter not in "abcdefghijklmnopqrstuvwxyz":
                        valid = False
        return valid


def word_to_guess() -> str:
        """Obtain a valid secret word from player 1.
        Parameters: None.
        Preconditions: Player 1 can enter the word privately.
        Returns a nonempty lowercase word containing only letters a-z.
        Postconditions: A valid secret word has been obtained.
        Steps: Request player 1's word using getpass. Remove surrounding spaces and convert it to lowercase. While valid_word rejects the word: display an error message, request and normalize another word and return the valid word.
        """
        secret_word = getpass("Player 1, enter the secret word: ").strip().lower()
        while not valid_word(secret_word):
                print("Please enter a nonempty word using letters a-z only")
                secret_word = getpass("Player 1, enter the secret word: ").strip().lower()
        return secret_word


def two_player() -> None:
        """Coordinate one two-player round.
        Parameters: None
        Preconditions: The shared play function is available.
        Returns: None
        Postconditions: Player 2's round has finished.
        Steps:get player 1's word using word_to_guess. Tell player 2 to begin guessing and call play with the secret word.
        """
        secret_word = word_to_guess()
        print("Player 2, you can begin guessing!")
        play(secret_word)
