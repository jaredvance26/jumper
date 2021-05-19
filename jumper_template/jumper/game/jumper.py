letters = []
word = 'red'

guess = input('what is your guess')
if guess in word:
    print('Wow')
else:
    print('failure')