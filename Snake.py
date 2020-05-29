from Direction import Direction
from Position import Position
import random
import math


class Snake:
    position = Position(0,0)
    position_history = []
    tail_length = 1
    step_size = 0
    direction = Direction.RIGHT

    def __init__(self, width, height, step_size):
        # randomize start position with safe distance to outer walls
        self.position.x = math.floor(random.randint(200, width - 200) / step_size) * step_size
        self.position.y = math.floor(random.randint(200, height - 200) / step_size) * step_size
        self.step_size = step_size

    def handle_movement(self, part):
        if self.direction == Direction.RIGHT:
            part.x += self.step_size
        elif self.direction == Direction.LEFT:
            part.x -= self.step_size
        elif self.direction == Direction.UP:
            part.y -= self.step_size
        elif self.direction == Direction.DOWN:
            part.y += self.step_size

    def step(self):
        if len(self.position_history) >= self.tail_length:
            self.position_history.pop(0)

        self.position_history.append(Position(self.position.x, self.position.y))
        self.handle_movement(self.position)

    def grow(self):
        self.tail_length += 1

    def get_center(self):
        return Position(int(self.position.x + (self.step_size/2)), int(self.position.y + (self.step_size/2)))

    def get_nose(self):
        nose = self.get_center()
        self.handle_movement(nose)
        return nose
