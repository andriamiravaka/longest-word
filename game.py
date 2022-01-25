from operator import truediv
import string
import random
class Game:
    def __init__(self):
        self.grid=[]
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
        
    def random_grid():
        pass
    
    def is_valid(self,word):
        if not word:
            return False
        letters=self.grid.copy() #maka ny lettre anatin;lay grid
        
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
    
        
    