class Position:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def collision(self, position):
        return self.x == position.x and self.y == position.y
