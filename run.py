import sys
import os
import time

grid = [' - ', ' - ', ' - ',
        ' - ', ' - ', ' - ',
        ' - ', ' - ', ' - ']

game_active = True  # Boolean to determine if game is active or finished
win = None  # variable will be updated when a win is determined
player = ' X '  # Sets the current player


def display_game_area():
    """
    Display and print the gaming area.
    """
    print('| ' + grid[0] + ' | ' + grid[1] + ' | ' + grid[2] + ' | ')
    print('| ' + grid[3] + ' | ' + grid[4] + ' | ' + grid[5] + ' | ')
    print('| ' + grid[6] + ' | ' + grid[7] + ' | ' + grid[8] + ' | ')


def current_player_input():
    """
    Request current player to input their grid slot within the
    grid area. Validation checks to ensure the input number is
    between 1-9. Converts this to an integer (and minus one to
    get correct index from grid list). Checks to see if
    grid slot has already been chosen. If all validation passes,
    the 'X' or 'O' character is placed in the grid slot chosen.
    """
    print("\nPlayer" + player + "turn")
    grid_slot = input("Enter grid number between 1-9:\n")

    valid_input = False

    while not valid_input:
        # check to see how to reduce the code
        while grid_slot not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("\nValue not accepted.")
            grid_slot = input("\nEnter grid number between 1-9:\n")

        grid_slot = int(grid_slot) - 1

        if grid[grid_slot] != ' - ':
            print("Position already taken.")
        else:
            valid_input = True

    grid[grid_slot] = player

    display_game_area()


def has_game_finished():
    """
    Function that checks if the game has been won or drawn
    by running two further functions.
    """
    check_if_winner()
    check_if_draw()


def check_if_winner():
    """
    Function to check if the game has been won by either
    matching 3 in a row, column or in a diagonal.
    """
    global win

    win_by_row = check_row()
    win_by_column = check_column()
    win_by_diagonal = check_diagonal()

    if win_by_row:
        win = win_by_row
    elif win_by_column:
        win = win_by_column
    elif win_by_diagonal:
        win = win_by_diagonal
    else:
        win = None


def check_row():
    """
    Check to see if there is a winning row.
    Checks to see if each grid index is the same in each
    row. Sets the global variable to False if there is a
    match to end game. And returns the character of the
    winning grid slot.
    """
    global game_active

    row1 = grid[0] == grid[1] == grid[2] != ' - '
    row2 = grid[3] == grid[4] == grid[5] != ' - '
    row3 = grid[6] == grid[7] == grid[8] != ' - '

    if row1 or row2 or row3:
        game_active = False

    if row1:
        return grid[0]
    elif row2:
        return grid[3]
    elif row3:
        return grid[6]
    else:
        return None


def check_column():
    """
    Check to see if there is a winning column.
    Checks to see if each grid index is the same in each
    column. Sets the global variable to False if there is
    a match to end game. And returns the character of the
    winning grid slot.
    """
    global game_active

    col1 = grid[0] == grid[3] == grid[6] != ' - '
    col2 = grid[1] == grid[4] == grid[7] != ' - '
    col3 = grid[2] == grid[5] == grid[8] != ' - '

    if col1 or col2 or col3:
        game_active = False

    if col1:
        return grid[0]
    elif col2:
        return grid[1]
    elif col3:
        return grid[2]
    else:
        return None


def check_diagonal():
    """
    Check to see if there is a winning diagonal.
    Checks to see if each grid index is the same in each
    diagonal. Sets the global variable to False if there
    is a match to end game. And returns the character of the
    winning grid slot.
    """
    global game_active

    diag1 = grid[0] == grid[4] == grid[8] != ' - '
    diag2 = grid[2] == grid[4] == grid[6] != ' - '

    if diag1 or diag2:
        game_active = False

    if diag1:
        return grid[0]
    elif diag2:
        return grid[2]
    else:
        return None


def check_if_draw():
    """
    Function to check if the game has no winner
    """
    global game_active

    if ' - ' not in grid:
        game_active = False


def change_player():
    """
    Function to check what the current player is and to
    change the global variable to the other player's input
    value in readiness for the next player's input.
    """
    global player

    if player == ' X ':
        player = ' O '
    elif player == ' O ':
        player = ' X '


def restart_game():
    """
    Function which prompts the users if they wish to restart
    the game. Answering yes with confirm game restarting,
    resets the grid and then runs the game after a 2 second
    delay. Answering no with quit the game.
    """
    global grid
    while True:
        answer = input("Restart game? Enter Y or N:\n")
        if answer.lower().startswith("y"):
            print("Game restarting...\n")
            time.sleep(2)
            grid = [' - ', ' - ', ' - ',
                    ' - ', ' - ', ' - ',
                    ' - ', ' - ', ' - ']
            os.execl(sys.executable, sys.executable, *sys.argv)
            play_game()
        elif answer.lower().startswith("n"):
            print("Thanks for playing!")
            sys.exit()


def play_game():
    """
    Start game
    """
    print("Welcome to Naughts & Crosses!\n")
    print("\033[1m" + "How to play." + "\033[0m")
    print("Enter a grid number between 1-9.")
    print("Grid numbers go left to right starting on the top row.")
    print("Number 1 is the top left position & number 9 is the bottom right.")
    print("\nPlayer X goes first. Good luck!\n")

    display_game_area()

    while game_active:

        current_player_input()

        has_game_finished()

        change_player()

    if win == " X ":
        print("\nPlayer " + win + " won.")
    elif win == " O ":
        print("\nPlayer " + win + " won.")
    else:
        print("\nThe game has ended in a draw.")

    restart_game()


play_game()
