# COMP 170 Final Project
# Assignment: Hang In There! Hangman Project
# Name and Loyola ID/email: Ela Ilic (00001662221) and Emujin Otgonbayar (00001767505)
# Date: November 24, 2026
#
# DESCRIPTION:
# A console Hangman game with single-player and two-player modes.
# Players guess letters or the entire word and may replay after a round.
#
# QUESTIONS:
# None.
#
# PROBLEM ANALYSIS & KEY ISSUES:
# The program must keep menu control separate from the player modes.
#
# PROGRAM PSEUDOCODE:
# First start main and display the instructions. Set the replay to true, while true: get a valid mode using mode_menu. If single-player was selected: get difficulty using difficulty_menu and call single_player with that difficulty, otherwise: call two_player. Update the replay using play_again and display the closing message.
#
# FUNCTIONS:
# instructions: Display the game rules
# mode_menu: Get a valid player mode
# play_again: Get the player's replay decision
# difficulty_menu: Get a valid single-player difficulty.
# main: Coordinate menus and repeated rounds.
#
# SETUP:
# Install the normal-word package with: python3 -m pip install random-word

#For one player mode: python3 -m pip install random-word

from one_player import single_player
from multiplayer import two_player


def instructions() -> None:
        """Display the game rules
        No parameters, preconditions, returns
        Postconditions are the printed instructions
        Steps: display the welcome message, explain the modes and single player difficulties.
        Next explain letter guesses and whole word guesses; explain winning, losing and invalid/repeated guesses.
        """
        print("""Welcome to Hang In There! By Scaly Syntax
The game is hangman, choose whether you want single-player or two-player mode.
Then choose your level - easy or hard.
Then a blank word with spaces will pop up.
Type your letter guess into the console and watch the drawing window.
If incorrect, your guess will add another limb.
You can guess one letter at a time or try the whole word.
A correct letter guess reveals all the matching positions.
Six incorrect letter guesses loses the game.
An incorrect whole gword guess causes an immediate loss.
Invalid and repeated guesses do not count toward your attempts.
Easy mode uses the most common English words and normal words can be anything.
Good luck and have fun!""")
        pass


def mode_menu() -> int:
        """Get valid player input for mode.
        No paramaters
        Precondtion: player input in console needs to be valid input of "1" or "2"
        Returns 1 for single player or 2 for two players
        Postconditions: Returned mode is either a 1 or 2
        Steps: ask player to enter "1" or "2", won't allow anything else. While the response is neither, ask again to enter and diplay error message.
        Then convert valid response to an integer and return it.
        """
        mode = input("Enter your desired mode: 1 = single-player, 2 = two-player: ")
        while mode != "1" and mode != "2":
                print("Enter either 1 or 2")
                mode = input("Enter your desired mode: 1 = single-player, 2 = two-player: ")
        return int(mode)


def play_again() -> bool:
        """Get the player's input decision to play again or not
        No parameters
        Preconditions: The player can enter console input.
        Returns True for y or False for n.
        Postconditions: A valid replay decision has gone through.
        Steps: Ask whether the player wants another round. While the response is neither y nor n: display an error message and ask again
        Return whether the response is y.
        """
        again = input("Play again? (y/n): ")
        while again != "y" and again != "n":
                print("Enter either y or n")
                again = input("Play again? (y/n): ")
        return again == "y"


def difficulty_menu() -> str:
        """Get a valid single-player difficulty.
        No parameters
        Preconditions: Single-player mode has been selected.
        Returns either "easy" or "hard".
        Postconditions: The returned difficulty is a supported choice.
        Steps: ask the player to enter easy or hard. While the response is neither option: display an error message and ask again.
        Return the selected difficulty
        """
        difficulty = input("Choose a difficulty: easy or hard: ")
        while difficulty != "easy" and difficulty != "hard":
                print("Enter either easy or hard")
                difficulty = input("Choose a difficulty: easy or hard: ")
        return difficulty

def main() -> None:
        """Coordinate the menus and repeated rounds.
        No parameters
        Preconditions: The required game modules are available.Returns: None
        Postconditions: A closing message has been displayed.
        Steps: display instructions, repeat the selected game mode while the player wants to play.
        Then ask about replay after each round and display the closing message.
        """
        instructions()
        keep_playing = True
        while keep_playing:
                mode = mode_menu()
                if mode == 1:
                        difficulty = difficulty_menu()
                        single_player(difficulty)
                else:
                        two_player()
        print("Thanks for playing Hang In There!")



#Test main function
if __name__ == "__main__":
        main()
