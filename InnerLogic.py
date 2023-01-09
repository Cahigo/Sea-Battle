from Exceptions import *

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    def __init__(self, bow, direct: bool, hp):
        self.bow = bow
        self.direct = direct  # 0 - Horizontal, 1 - Vertical
        self.hp = hp

    @property
    def dots(self, size):
        ship_dots = []
        for i in range(self.hp):
            current_x = self.bow.x
            current_y = self.bow.y
            if self.direct == 0:
                current_x += i
            elif self.direct == 1:
                current_y += i
            ship_dots.append(Dot(current_x, current_y))

    def hit(self, shot):
          return shot in self.dots

class Board:
    def __init__(self, hid: bool, size = 6):
        self.size = size
        self.hid = hid

        self.field = [["O"] * size for _ in range(size)]

        self.used = []
        self.ships = []

    def __str__(self):
        board = ""
        board += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            board += f"\n{i + 1} | " + " | ".join(row) + " | "

        if self.hid:
            board = board.replace("O", "F")

        return board

    def out(self, d: Dot):
        return not (0 <= d.x < self.size) and (0 <= d.y < self.size)

    def contour(self): # Draw a contour around ship


    def board_print(self):

    def out(self):

    def shot(self):
