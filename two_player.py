#Multiplayer

from getpass import getpass
from one_player import play

def valid_word(word: str) -> bool:
        """Return whether word contains only lowercase letters a through z."""
        valid = len(word) > 0
        for letter in word:
                if letter not in "abcdefghijklmnopqrstuvwxyz":
                        valid = False
        return valid

def word_to_guess() -> str:
        """Ask for word from the two player and determines whether valid/invalid
 input, no parameters, returns a string that is a valid lowercase secret word cho
sen by player 1"""
#Ask player 2 to not look and repeat getpass(0 to read player 1's word without displaying it and removing the surrounding spaces/convert to lowercase
#f it is nonempty and contains only characters a-z then return word, otherwise return invalid word message
        secret_word = getpass("Player 1, enter the secret word: ").strip().lower()
        while not valid_word(secret_word):
                print("Please enter a nonempty word using letters a-z only")
                secret_word = getpass("Player 1, enter the secret word: ").strip().lower()
        return secret_word

def two_player() -> None:
        """Use the player 1 play style, no parameter, no returns"""
#Get the secret word using the word_to_guess() and tell player 2 to begin guessing, call play(secret_word)
        secret_word = word_to_guess()
        print("Player 2, you can begin guessing!")
        play(secret_word)
