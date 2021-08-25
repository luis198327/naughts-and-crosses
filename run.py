grid = [' - ', ' - ', ' - ',
        ' - ', ' - ', ' - ',
        ' - ', ' - ', ' - ']

game_active = True  # Boolean to determine if game is active or finished


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

    grid[grid_slot] = ' X '

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
    Function to check if the game has been won by either matching
    3 in a row, column or in a diagonal.
    """
    win = None

    win_by_row = check_row()
    win_by_column = check_column()
    win_by_diagonal = check_diagonal()

    if win_by_row:
        win = check_row()
    elif win_by_column:
        win = check_column()
    elif win_by_diagonal:
        win = check_diagonal()
    else:
        win = None  
    return win


def check_row():
    """
    Check to see if there is a winning row. Checks to see if
    each grid index is the same in each row. Sets the
    global variable to False if there is a match to end game.
    """
    global game_active

    row1 = grid[0] == grid[1] == grid[2]
    row2 = grid[3] == grid[4] == grid[5]
    row3 = grid[6] == grid[7] == grid[8]

    if row1 or row2 or row3:
        game_active = False


def check_column():
    """
    Check to see if there is a winning column. Checks to see if
    each grid index is the same in each column. Sets the
    global variable to False if there is a match to end game.
    """
    global game_active

    col1 = grid[0] == grid[3] == grid[6]
    col2 = grid[1] == grid[4] == grid[7]
    col3 = grid[2] == grid[5] == grid[8]

    if col1 or col2 or col3:
        game_active = False


# def check_diagonal():


def check_if_draw():
    return


def change_player():
    return


def play_game():
    """
    Start game
    """
    display_game_area()

    while game_active:

        current_player_input()

        has_game_finished()

        change_player()


play_game()


# def restart_game():
