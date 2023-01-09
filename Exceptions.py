class DotIsOutException(Exception):  # If coordinates are out of the game board
    def __str__(self):
        return "Dot is out of the board"


class ShipIsOutException(Exception):  # If ship's placement is out of game board
    def __str__(self):
        return "Ship placement is out of the board"


class ShotIsOutException(Exception):  # If shot is out of game board
    def __str__(self):
        return "Shot is out of the board"


class ShotWasDealtException(Exception):  # If empty dot already was shot
    def __str__(self):
        return "This dot was already shot"
