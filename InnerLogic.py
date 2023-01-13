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
    def __init__(self, bow, direct, hp):
        self.bow = bow
        self.direct = direct  # 0 - Horizontal, 1 - Vertical
        self.hp = hp

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.hp):
            current_x = self.bow.x
            current_y = self.bow.y
            if self.direct == 0:
                current_x += i
            elif self.direct == 1:
                current_y += i
            ship_dots.append(Dot(current_x, current_y))
        return ship_dots

    def hit(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid  # Is board hidden (for AI board)

        self.sunken = 0  # For sunken ships
        self.field = [["O"] * size for i in range(size)]

        self.used = []
        self.ships = []

    def __str__(self):  # Board printing
        board = ""
        board += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            board += f"\n{i + 1} | " + " | ".join(row) + " | "

        if self.hid:
            board = board.replace("O", "F")
            board = board.replace("♠", "F")

        return board

    def out(self, d: Dot):  # Check if dot is out of border
        return not((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, hid=True):  # Draw a contour around ship
        contour = [[1, -1], [1, 0], [1, 1],
                   [0, -1], [0, 0], [0, 1],
                   [-1, -1], [-1, 0], [-1, 1]]

        for d in ship.dots:
            for dx, dy in contour:
                current = Dot(d.x + dx, d.y + dy)  # Testing dot
                if not (self.out(current)) and current not in self.used:  # If this dot isn't out of board AND not used
                    if not hid:
                        self.field[current.x][current.y] = "."  # Draw a contour
                    self.used.append(current)  # Add this dot in "used" list

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.used:
                raise ShipIsOutException

        for d in ship.dots:
            if not self.hid:
                self.field[d.x][d.y] = "♠"
            self.used.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out(d):
            raise ShotIsOutException
        if d in self.used:
            raise ShotWasDealtException

        self.used.append(d)

        for ship in self.ships:
            if ship.hit(d):
                ship.hp -= 1
                self.field[d.x][d.y] = "x"
                if ship.hp == 0:
                    self.sunken += 1
                    self.contour(ship, hid=False)  # For sunken ships we draw a contour
                    print("Ship was destroyed!")
                    return False
                else:
                    print("Ship was damaged!")
                    return True

        self.field[d.x][d.y] = "m"
        print("Missed!")
        return False

    def clean_used(self):
        self.used = []
