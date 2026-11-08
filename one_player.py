#One player
#Program Structure

import random

#Drawing ASCII: have seven drawings for each mistake and outputs when mistake is done

def get_word(difficulty: str) -> str:
        """Create lists based on difficulty options, parameters are the difficulty modes: "easy" or "normal", the return is a random word from the difficulty group"""
#Create a list of easy words and normal words
#If the difficulty is easy return word from easy list, otherwise return word from normal list
        pass

def single_player(difficulty: str) -> None:
        """Paramteters are the difficulty as strings, either easy or normal, no returns"""
#Get the secret word using the get_word and call play_game of the secret word
        pass

def guess(guessed_letters: list[str], guessed_words: list[str]) -> str:
        """Ask for letter/word and displey if present or invlaid/repeated guess, parameters guessed_letters in the string list of previously guessed letters and guessed_words in the string list of previously guessed whole words, returns a valid new lowecase letter or whole word guess"""
#Repeat asking for letter/whole word guess and remove spaces/convert to lowercase, if empty/uses character outside a-z display invalid input, otherwise if guess already made display repeated guess, otherwise return the guess
        pass

def display(secret_word: str, guessed_letters: list[str], guessed_words: list[str], mistakes: int, reveal_word: bool = False) -> None:
        """Goes through letter to see if it is in word with output of letter, paramters is the string of secret_word that is being guessed, the list of string for the guessed_letters of previously guessed letters, the guessed_words as a list of strings for the guessed whole words, mistakes as an integer of number of incorrect guessed (0-6), and the reveal_word as a boolean to show the full word if True, no returns"""
#print the hangman[mistakes]
#For each letter in secret_word if the letter was guessed/reveal_word = True, show the letter otherwise just show an underscore, need to pint spaces between the displayed characters
#Print previously guessed letters and words and the remaining guesses (6- mistakes already made)
        pass

def check_win(secret_word: str, guessed_letters: list[str], guessed_words: list[str]) -> bool:
        """Checks if it is a win of all the letters guessed or if the word was guessed, parameters are the string of the secret_word being guessed, the guessed_letters as a string in a list of previously guessed letters, and guessed_words in a string list of previously guessed whole words, returns the boolean True if the player won, otherwise is False"""
#If the secret_word is in guessed_words return True and for each letter in secret_word if the letter is in the guessed_letters return True, otherwise return False
        pass

def play(secret_word: str) -> None:
        """Go through guesses and see if they are correct/incorrect and updates guess list and hangman drawing, parameter is the secret_word as a string that is the lowercase word being guessed, returns none"""
#Create empty guessed_letters and guessed_words lists and set mistakes to 0
#While the mistakes are less than 6, call display() with the current game and get a new guess()
#If the guess is one letter, add it to the guessed_letters and check if it appears in the secret_word, otherwise add it to the guessed words and see if it equals the secret_word
#If the guess is correct show the correct guess letter/where/and the message correct, otheriwse increase the mistake by 1 and add to the guessed, diaplay the incorrect guess message
#If the guess if a whole word, add it to guessed_words. If the guess == secret_word, display the correct word message exit the loop, otherwise display incorrect word message and exit loop. 
#If check_win() is True then exit the loop
#Class display() with reveal_word = True and if check_win() is True then say you win, otherwise display a you lose and the correct secret_word
        pass
