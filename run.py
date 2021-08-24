grid = [' - ', ' - ', ' - ',
        ' - ', ' - ', ' - ',
        ' - ', ' - ', ' - ']


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
    grid area. Changes to integer and minus one to get correct
    index from grid list
    """
    grid_slot = int(input("\nEnter grid number between 1-9:\n"))-1

    grid[grid_slot] = ' X '

    display_game_area()


def play_game():
    """
    Start game
    """
    display_game_area()

    current_player_input()


play_game()







# Initial Code functions required:

# def change_player():

# def has_game_finished():

# def check_if_winner():

# def check_row():

# def check_column():

# def check_diagonal():

# def check_if_draw():

# def restart_game():
