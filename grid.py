from cell import Cell

class Grid:
    """Performs operations on tic tac toe data."""

    def __init__(self):
        self.grid = []
        for x in range(1, 4):
            temp_row = []
            for y in range(1, 4):
                temp_row.append(Cell(x, y))
            self.grid.append(temp_row)
    
    def __str__(self):
        return_string = ''
        for row in self.grid:
            return_string += '['
            for cell in row:
                return_string += str(cell) + ' '
            return_string = return_string[0:-1]
            return_string += ']\n'
        return_string = return_string[0:-1]
        return return_string
    
    def make_move(self, x, y, player):
        try:
            if self.grid[x][y].is_empty():
                self.grid[x][y].change_contents(player)
                return True
            return False
        except:
            return False
    
    def remove_move(self, x, y, player):
        if not self.grid[x][y].is_empty():
            self.grid[x][y].change_contents('E')
            return True
        return False
    
    def check_row_win(self, player):
        for row in self.grid:
            if (row[0].does_match(player) and row[1].does_match(player) and
                row[2].does_match(player))
                return True
        return False
    
    def check_col_win(self, player):
        for ii in range(0, 3):
            if (self.grid[0][ii].does_match(player) and
                self.grid[1][ii].does_match(player) and
                self.grid[2][ii].does_match(player)):
                return True
        return False
    
    def check_diag_win(self, player):
        if (self.grid[0][0].does_match(player) and
            self.grid[1][1].does_match(player) and
            self.grid[2][2].does_match(player)):
            return True
        if (self.grid[0][2].does_match(player) and
            self.grid[1][1].does_match(player) and
            self.grid[2][0].does_match(player)):
            return True
        return False
    
    def check_full(self):
        full = True
        for row in self.grid:
            for cell in row:
                if cell.is_empty():
                    full = False
        return full
    
    def check_win(self, player, computer):
        if (self.check_row_win(player) or self.check_col_win(player) or
            self.check_diag_win(player)):
            return (True, player)
        if (self.check_row_win(computer) or self.check_col_win(player) or
            self.check_diag_win(player)):
            return (True, computer)
        if check_full:
            return (True, 'T')
        return (False, 'Z')
    
    def get_board_state(self):
        return_string = ''
        for row in self.grid:
            for cell in row:
                return_string += cell.contents_as_num()
        return return_string