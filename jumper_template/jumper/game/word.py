import random

class Word:
    """
    Selects word randomly and tracks the guesses. Calculates if you win or not.
    Sterotype: Info Holder
     """
    def __init__(self):
        self.words = ['light', 'apple', 'characterization', 'table']

    def get_word(self):
        self.rand_word = random.choice(self.words)
        self.guessed = []
        for char in self.rand_word:
            self.guessed.append('_')
        

    def char_num(self):
        self.num = len(self.rand_word)
        if not '_' in self.guessed:
            return True
        else:
            return False



    def compare_letter(self, guess):
        x = 0
        success = False
        for i in self.rand_word:
            if guess == i:
                self.guessed[x] = guess
                success = True
            x += 1
        return success
    

