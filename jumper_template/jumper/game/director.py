from game.director import Director
from game.console import Console
from game.jumper import Jumper
from game.word import Word

class Director:
    """ The purpose of this class is to direct and control the flow of the game.
    Stereotype: Controller

    """
    def __init__(self):
        self.director = Director()
        self.console = Console()
        self.jumper = Jumper()
        self.word = Word()
        self.keep_playing = True
    
    def get_inputs(self):
        pass

    def get_updates(self):
        pass

    def get_output(self):
        pass

