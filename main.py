#Hangman code
#Program structure


from player1 import single_player
from multiplayer import two_player

def instructions() -> None:
        """ Display game instructions, no parameters or returns"""
#Print the welcome message and the difficulty levels with mode options
#Players guess one letter at a time and can also guess the whole word (if wrong, insta lose)
#Wrong guesses adds limbs to the drawing, and 6 wrongs lose, while repeated/invalid guessses dont count
        pass

def mode_menu() -> tuple[int, str]:
        """Gives option for difficulty and player mode, no parameters, returns game mode (1 or 2) and difficulty ("easy" or "normal")"""
#Repeat until valid mode is entered (1: single player, 2: two-player), if valid store as integer and exit loop, otherwise display error
#If mode is 1, Repeat until valid difficulty is entered (easy ornormal),  remove spaces/convert to lowercase and if valid store and exit loop, otherwise display error
#If mode is 2, set difficulty to an empty string
#Return the mode and difficulty
        pass

def play_again() -> bool:
        """Ask to play again, no parameters and returns true to play again or false to quit"""
#Repeat till valid input, ask to play again (yes or no), if yes then return True, if no then return False, otherwise display error
        pass

def main() -> None:
        """Calls everything, no parameters and no returns"""
#Call instructions(), repeat till valid: get mode and difficulty from mode_menu(), mode 1 = single_player(difficulty), otherwise mode 2 = two_player(difficulty), if play_again is False exit the loop
#Display end message
        pass

#Call main function
if __name__ == "__main__":
        main()
