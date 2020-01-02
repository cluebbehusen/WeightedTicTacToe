from grid import Grid
from computer import Computer

valid_user_selections = 'xXoO'

def gather_user_input():
    """Gathers coordinates from user and determines validity."""
    x = 0
    y = 0
    while True:
        try:
            x = int(input('Enter your desired x coordinate: '))
            if x < 0:  # Avoid issues with negative indexes being used
                raise ValueError
            y = int(input('Enter your desired y coordinate: '))
            if y < 0:
                raise ValueError
        except ValueError:
            print('Invalid input.')
        else:
            break
    return x, y

if __name__ == '__main__':
    
    main_grid = Grid()
    
    user_selection = 'z'
    while user_selection not in valid_user_selections:
        user_selection = input('Enter your desired character (x or o): ')
    user_selection = user_selection.upper()
    if user_selection == 'X':
        user_char = 'X'
        computer_char = 'O'
    else:
        user_char = 'O'
        computer_char = 'X'
    
    computer = Computer("weights.csv", computer_char)
    
    current_move = 'X'
    win, winner = main_grid.check_win(user_char, computer_char)
    while not win:
        if current_move == user_char:
            print('= Grid =')
            print(main_grid)
            x, y = gather_user_input()
            while not main_grid.make_move(x, y, user_char):
                print('Invalid input.')
                x, y = gather_user_input()
            current_move = computer_char
        elif current_move == computer_char:
            computer.make_move(main_grid)
            current_move = user_char
        win, winner = main_grid.check_win(user_char, computer_char)
    
    print(main_grid)
    if winner == computer_char:
        print('The computer won.')
        computer.update_csv('W')
    elif winner == user_char:
        print('You won.')
        computer.update_csv('L')
    elif winner == 'T':
        print('Tie.')
        computer.update_csv('T')
    
