#Hangman code
#Program structure

#For one player mode: python3 -m pip install random-word
from one_player import single_player
from multiplayer import two_player

def instructions() -> None:
        """ Display game instructions, no parameters or returns"""
#Print the welcome message and the difficulty levels with mode options
#Players guess one letter at a time and can also guess the whole word (if wrong, insta lose)
#Wrong guesses adds limbs to the drawing, and 6 wrongs lose, while repeated/invalid guessses dont count
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
        """Gives option for difficulty and player mode, no parameters, returns game mode (1 or 2) and difficulty ("easy" or "normal")"""
#Repeat until valid mode is entered (1: single player, 2: two-player), if valid store as integer and exit loop, otherwise display error
#Repeat until valid difficulty is entered (easy ornormal),remove spaces/convert to lowercase and if valid store and exit loop, otherwise display error
#Return the mode and difficulty
        mode = input("Enter your desired mode: 1 = single-player, 2 = two-player: ")
        while mode != "1" and mode != "2":
                print("Enter either 1 or 2")
                mode = input("Enter your desired mode: 1 = single-player, 2 = two-player: ")
        return int(mode)

def play_again() -> bool:
        """Ask to play again, no parameters and returns true to play again or false to quit"""
#Repeat till valid input, ask to play again (yes or no), if yes then return True, if no then return False, otherwise display error
        again = input("Play again? (y/n): ")
        while again != "y" and again != "n":
                print("Enter either y or n")
                again = input("Play again? (y/n): ")
        return again == "y"

def difficulty_menu() -> str:
        """Return either easy or normal difficulty
        Ask user for input and accept only easy or normal
        Return the difficulty"""
        difficulty = input("Choose a difficulty: easy or hard: ")
        while difficulty != "easy" and difficulty != "hard":
                print("Enter either easy or hard")
                difficulty = input("Choose a difficulty: easy or hard: ")
        return difficulty

def main() -> None:
        """Calls everything, no parameters and no returns"""
#Call instructions(), repeat till valid: get mode and difficulty from mode_menu(), mode 1 = single_player(difficulty), otherwise mode 2 = two_player(difficulty), if play_again is False exit the loop
#Display end message
        instructions()
        keep_playing = True
        player_round = False
        while keep_playing:
                mode = mode_menu()
                if mode == 1:
                        difficulty = difficulty_menu()
                        single_player(difficulty)
                        player_round = True
                        keep_playing = play_again()
                else:
                        two_player()
                        player_round = True
                        keep_playing = play_again()
        print("Thanks for playing Hang In There!")

#Test main function
if __name__ == "__main__":
        main()
