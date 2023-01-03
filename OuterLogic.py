from InnerLogic import Board

class Player:  # Parent class for AI and User classes
    def __init__(self, myboard, otherboard):
        self.myboard = myboard
        self.otherboard = otherboard

    def ask(self, dot):
        return None

    def move(self, board: Board):
        self.ask()
        board.shot()
        return True

class AI(Player):

class User(Player):

class Game:
    def __init__(self, user: User, userboard: Board, ai: AI, aiboard: Board):
        self.user = user;
        self.userboard = userboard
        self.ai = ai
        self.aiboard = aiboard

    def random_board(self): # Board generator
        return None

    def greet(self):
        return None

    def loop(self):
        return None

    def start(self):
        self.greet()
        self.loop()

#---------------------------------------------

Game.start()
