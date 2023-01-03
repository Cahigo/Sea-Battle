from Exceptions import BoardOutException

class Dot:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def Coordinates(self):
        return self._x and self._y

    @Coordinates.setter
    def Coordinates(self, x, y):
        if (1 <= x <= 6) and ((1 <= y <= 6)):
            self._x = x
            self._y = y
        else:
            raise BoardOutException("Value must be between 1..6")

class Ship:
    def __init__(self, size, bow, direction, hp):
        self.size = size;
        self.bow = bow;
        self.direction = direction
        self.hp = hp

    def dots(self, size, hp):
        return size - hp

class Board:
    def __init__(self, board, ships_all, hid: bool, ships_remain):
        self.board = board
        self.ships_all = ships_all
        self.hid = hid
        self.ships_remain = ships_remain

    @property
    def add_ship(self):
        return self._ships_all

    @add_ship.setter
    def add_ship(self, ship):
        self.ships_all += ship
    def contour(self): # Draw a contour around ship

    def board_print(self):

    def out(self):

    def shot(self):
