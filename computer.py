import random

AGGRESSION_VALUE = .6  # This value determines the willingness of the computer
                       #    to play moves it has never encountered before.
                       #    It must be a number between 0 and 1

class Computer:
    """Makes move based off csv file and updates it accordingly"""
    
    def __init__(self, file, char):
        """Initializes dictionary of past used moves and their weights."""
        self.available_board_states = dict()
        self.used_board_states = []
        self.file = file
        self.char = char
        try:
            with open(self.file, 'r') as weights:
                for line in weights:
                    grid, freq, total, weight = line.split(', ')
                    weight = float(weight.replace('\n', ''))
                    freq = float(freq)
                    total = float(total)
                    self.available_board_states[grid] = (freq, total, weight)
        except FileNotFoundError:
            print('Given file not found. Creating new file.')
        # open(self.file, 'w').close()
    
    def get_weight(self, grid, board_state):
        """Gathers the weight of a potential move"""
        if board_state in self.available_board_states:
            return self.available_board_states[board_state][2]
        else:
            return AGGRESSION_VALUE
    
    def make_move(self, grid):
        """Makes move on grid based on weights of each possible move."""
        highest_weight = 0
        possible_moves = []
        available_moves = {}
        for ii in range(0, 3):
            for jj in range(0, 3):
                if grid.make_move(ii, jj, self.char):
                    board_state = grid.get_board_state(self.char)
                    weight = self.get_weight(grid, board_state)
                    available_moves[board_state] = weight
                    if weight > highest_weight:
                        highest_weight = weight
                    grid.remove_move(ii, jj, self.char)
        for board_state in available_moves:
            if available_moves[board_state] == highest_weight:
                possible_moves.append(board_state)
        if len(possible_moves) == 1:
            move = possible_moves[0]
        else:
            rand_index = random.randint(0, len(possible_moves) - 1)
            move = possible_moves[rand_index]
        for ii in range(0, 3):
            for jj in range(0, 3):
                if grid.make_move(ii, jj, self.char):
                    if grid.get_board_state(self.char) == move:
                        self.available_board_states[move] = (0, 0, .6)
                        self.used_board_states.append(move)
                        return
                    else:
                        grid.remove_move(ii, jj, self.char)
        
    def update_csv(self, ending_condition):
        """Updates .csv file at end of game based on game outcome."""
        if ending_condition == 'W':
            w_num = 1.0
        elif ending_condition == 'T':
            w_num = .5
        else:
            w_num = 0.0
        with open(self.file, 'w') as weights:
            for board_state in self.available_board_states:
                if board_state in self.used_board_states:
                    weight = self.available_board_states[board_state][0] + w_num
                    freq = self.available_board_states[board_state][0] + 1.0
                    total = (weight / freq)
                else:
                    weight = self.available_board_states[board_state][0]
                    freq = self.available_board_states[board_state][1]
                    total = (weight/freq)
                print('{}, {}, {}, {}'.format(board_state, weight, freq, total),
                      file = weights)
    
