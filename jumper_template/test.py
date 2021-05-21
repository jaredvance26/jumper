# from jumper.word import Word

# word = Word()
# word.get_word()

# word.compare_letter('a')
# word.compare_letter('p')

# print(word.compare_letter('p'))
import random

def get_word():
    words = ['light', 'apple', 'characterization', 'table']
    rand_word = random.choice( words)
    guessed = []
    for char in  rand_word:
        guessed.append('_')
    print()
    print(' '.join(guessed))
    print()

get_word()

