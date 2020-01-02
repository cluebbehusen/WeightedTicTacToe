class Cell:
    """Holds information about each individual cell in tic tac toe grid."""

    def __init__(self, x, y):
        """Initializes an empty cell."""
        self.x = x
        self.y = y
        self.contents = 'E'
    
    def __str__(self):
        """Returns it contents in string form."""
        if self.contents == 'E':
            return '-'
        return self.contents
    
    def is_empty(self):
        """Returns true if the cell is empty, false otherwise."""
        if self.contents == 'E':
            return True
        return False
    
    def does_match(self, char):
        """Returns true if cell matches the given character, false otherwise."""
        if self.contents == char:
            return True
        return False
    
    def change_contents(self, char):
        """Changes cell contents to the provided character."""
        self.contents = char
    
    def contents_as_num(self, computer_char):
        """Returns the cell contents in number form for weighting purposes."""
        if self.contents == 'E':
            return '0'
        elif self.contents == computer_char:
            return '1'
        else:
            return '2'