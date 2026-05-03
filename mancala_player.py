class Player:
    Size = 6
    def __init__(self, order:int):
        self.Holes = [4] * self.Size   # each player gets their own list
        self.Order = order
        self.Mancala = 0