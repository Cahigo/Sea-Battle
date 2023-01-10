from Exceptions import *
from InnerLogic import *
from random import *

class Player:  # Parent class for AI and User classes
    def __init__(self, myboard, enemyboard):
        self.myboard = myboard
        self.enemyboard = enemyboard

    def ask(self):
        return None

    def move(self, board):
        if board.shot(self.ask()):
            return True
        return False

class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Enemy's turn: Dot({d.x + 1}, {d.y + 1})")
        return d

class User(Player):
    def ask(self):
        while True:
            coordinates = input("Type X and Y coordinates, Commander!").split()

            if len(coordinates) != 2:
                print("We need two coordinates, Commander!")
                continue

            x, y = coordinates
            if not(x.isdigit()) or not(y.isdigit()):
                print("Coordinates must be digits, Commander!")
                continue

            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)

class Game:
    def __init__(self, user, userboard, ai, aiboard):
        self.user = user;
        self.userboard = userboard
        self.ai = ai
        self.aiboard = aiboard

    def random_board(self): # Board generator


    def greet(self):
        return None

    def loop(self):
        return None

    def start(self):
        self.greet()
        self.loop()

#---------------------------------------------


