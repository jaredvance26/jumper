
from game.console import Console
from game.jumper import Jumper
from game.word import Word

class Director:
    """ The purpose of this class is to direct and control the flow of the game.
    Stereotype: Controller

    """
    def __init__(self):

        self.console = Console()
        self.jumper = Jumper()
        self.word = Word()
        self.keep_playing = True

    def start_game(self):
        self.word.get_word()
        while self.keep_playing:
            self.get_outputs()
            self.get_inputs()
            self.get_updates()
            
    
    def get_inputs(self):
        self.guess = self.console.write('Guess a letter [a-z]: ')


    def get_updates(self):
        success = self.word.compare_letter(self.guess)
        self.jumper.life_tracker(success)
        
        if self.word.char_num():
            print()
            print('You are a winner!')
            self.get_outputs()
            self.keep_playing = False

        if self.jumper.life == 4:
            print()
            print('Game Over!')
            self.get_outputs()
            self.keep_playing = False



    def get_outputs(self):
        self.console.show_word(self.word.guessed)
        self.console.show_message(self.jumper.parachute[self.jumper.life])

