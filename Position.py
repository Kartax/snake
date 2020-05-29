class Position:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("{}/{}".format(self.x, self.y))
