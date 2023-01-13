from random import *

from InnerLogic import *


class Player:  # Parent class for AI and User classes
    def __init__(self, myboard, enemyboard):
        self.myboard = myboard
        self.enemyboard = enemyboard

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                target = self.enemyboard.shot(self.ask())
                return target
            except ShotIsOutException as err:
                print(err)


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
            if not (x.isdigit()) or not (y.isdigit()):
                print("Coordinates must be digits, Commander!")
                continue

            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)


class Game:
    def random_board(self):  # Board generator
        board = None
        while board is None:
            ships = [3, 2, 2, 1, 1, 1, 1]
            board = Board(size=self.size)
            attempt = 0
            for i in ships:
                for j in range(1000):  # Tries
                    ship = Ship(Dot(randint(0, 5), randint(0, 5)),  # Bow
                                randint(0, 1),  # Direction
                                i)  # HP
                    try:
                        board.add_ship(ship)
                        break
                    except ShipIsOutException:
                        pass
            board.clean_used()
        return board

    def __init__(self, size=6):
        self.size = size
        plrboard = self.random_board()
        aiboard = self.random_board()
        aiboard.hid = True

        self.player = User(plrboard, aiboard)
        self.ai = AI(aiboard, plrboard)

    def greet(self):
        print("---Sea Battle---")
        print("Type coordinates in format: x y \n x - horizontal \n y - vertical \n")

    def loop(self):
        turn = 1
        while True:
            print("Player's board:")
            print(self.player.myboard)
            print("(-)" * 9)
            print("Computer's board:")
            print(self.ai.myboard)
            if turn == 1:
                print("Your turn!")
                if self.player.move():
                    turn = 1
                else:
                    turn = 0
            else:
                print("Computer's turn!")
                if self.ai.move():
                    turn = 0
                else:
                    turn = 1

            if self.ai.myboard.sunken == 7:
                print("(-)" * 9)
                print("Player win!")
                break

            if self.player.myboard.sunken == 7:
                print("(-)" * 9)
                print("Computer win!")
                break

    def start(self):
        self.greet()
        self.loop()
