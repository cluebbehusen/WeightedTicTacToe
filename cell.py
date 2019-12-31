class Cell:
    """Holds information about each individual cell in tic tac toe grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = 'E'
    
    def __str__(self):
        if self.contents == 'E':
            return '-'
        return self.contents
    
    def is_empty(self):
        if self.contents == 'E':
            return True
        return False
    
    def does_match(self, char):
        if self.contents == char:
            return True
        return False
    
    def change_contents(self, char):
        self.contents == char
    
    def contents_as_num(self):
        if self.contents == 'E':
            return '0'
        elif self.contents == 'X':
            return '1'
        elif self.contents == 'O':
            return '2'