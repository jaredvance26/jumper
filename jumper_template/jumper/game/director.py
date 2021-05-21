from game.director import Director
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
        while self.keep_playing:
            self.get_inputs()
            self.get_updates()
            self.get_outputs()
    
    def get_inputs(self):
        self.word.get_word()
        self.jumper.display()

    def get_updates(self):
        guess = self.console.write_message('Guess a letter [a-z]: ')
        self.word.compare_letter(guess)


    def get_outputs(self):
        pass

