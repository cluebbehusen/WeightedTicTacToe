class Cell:

    def __init__(self):
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