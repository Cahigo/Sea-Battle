class BoardOutException(Exception): # If coordinates are out of the game board
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"BoardOutExceptions, {self.message}"
        else:
            return "BoardOutException has been raised"

class ShipIsOutException(Exception): # If ship's placement is out of game board
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"ShipIsOutException, {self.message}"
        else:
            return "ShipIsOutException has been raised"

class ShotIsOutException(Exception): # If shot is out of game board
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"ShotIsOutException, {self.message}"
        else:
            return "ShotIsOutException has been raised"
