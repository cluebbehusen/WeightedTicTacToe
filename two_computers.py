from computer import Computer
from grid import Grid

import random
import sys

PRINT_OUTPUTS = False  # This boolean determines whether each move is outputted

if len(sys.argv) != 4:
    print('Invalid usage.')
    print('Usage: python3 two_computers.py [.csv file 1] [.csv file 2] [num]')
    sys.exit(1)

csv_file1 = sys.argv[1]
csv_file2 = sys.argv[2]
num_games = int(sys.argv[3])

games_played = 0

while games_played < num_games:
    
    main_grid = Grid()
    first_move = random.randint(0, 1)
    if first_move == 0:
        computer1_char = 'X'
        computer2_char = 'O'
    else:
        computer1_char = 'O'
        computer2_char = 'X'
    
    computer1 = Computer(csv_file1, computer1_char, True)
    computer2 = Computer(csv_file2, computer2_char, True)
    
    current_move = 'X'
    win, winner = main_grid.check_win(computer1_char, computer2_char)
    while not win:
        if current_move == computer1_char:
            computer1.make_move(main_grid)
            current_move = computer2_char
        elif current_move == computer2_char:
            computer2.make_move(main_grid)
            current_move = computer1_char
        if PRINT_OUTPUTS:
            print('= Grid =')
            print(main_grid)
        win, winner = main_grid.check_win(computer1_char, computer2_char)
    
    if winner == computer1_char:
        # print('Computer 1 won.')
        computer1.update_csv('W')
        computer2.update_csv('L')
    elif winner == computer2_char:
        # print('Computer 2 won.')
        computer1.update_csv('L')
        computer2.update_csv('W')
    elif winner == 'T':
        # print('Tie.')
        computer1.update_csv('T')
        computer2.update_csv('T')
    games_played += 1
    # print('Played games: {}/{}'.format(games_played, num_games))
