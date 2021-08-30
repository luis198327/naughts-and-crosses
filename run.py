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
    grid area. Change to integer and minus one to get correct
    index from grid list. Places character in grid slot.
    """
    grid_slot = int(input("\nEnter grid number between 1-9:\n"))-1

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


def play_game():
    """
    Start game
    """
    display_game_area()

    while game_active:

        current_player_input()

        has_game_finished()

        change_player()

    if win == " X ":
        print("Player " + win + " won.")
    elif win == " O ":
        print("Player " + win + " won.")
    else:
        print("The game has ended in a draw.")


play_game()


# def restart_game():
