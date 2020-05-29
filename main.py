import pygame
import random
import math
from Snake import Snake
from Direction import Direction
from Position import Position

width = 800
height = 800
block_size = 10

display = pygame.display.set_mode((width, height))
snake = Snake(width, height, block_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")
fruit = Position(0,0)

def draw_grid():
    for h in range(block_size, height, block_size):
        # horizontal
        pygame.draw.line(display, (50, 50, 50), (0, h), (width, h))
    for v in range(block_size, width, block_size):
        # vertical
        pygame.draw.line(display, (50, 50, 50), (v, 0), (v, height))


def draw_snake():
    snake_center = snake.get_center()
    nose = snake.get_nose()
    # tail
    for p in snake.position_history:
        pygame.draw.rect(display, (155, 0, 0), (p.x, p.y, block_size, block_size))
    # nose
    pygame.draw.line(display, (255, 0, 0), (snake_center.x, snake_center.y), (nose.x, nose.y))
    # body
    pygame.draw.rect(display, (255, 0, 0), (snake.position.x, snake.position.y, block_size, block_size))


def draw_fruit():
    pygame.draw.rect(display, (0, 255, 255), (fruit.x, fruit.y, block_size, block_size))


def move_fruit():
    fruit.x = math.floor(random.randint(0, width - block_size) / block_size) * block_size
    fruit.y = math.floor(random.randint(0, width - block_size) / block_size) * block_size


def main():

    running = True
    while running:
        # draw background
        display.fill((0, 0, 0))

        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = Direction.UP
                if event.key == pygame.K_DOWN:
                    snake.direction = Direction.DOWN
                if event.key == pygame.K_RIGHT:
                    snake.direction = Direction.RIGHT
                if event.key == pygame.K_LEFT:
                    snake.direction = Direction.LEFT
                if event.key == pygame.K_SPACE:
                    snake.grow()

        draw_grid()
        draw_fruit()
        draw_snake()

        # check fro collision with fruit
        if snake.position.x == fruit.x and snake.position.y == fruit.y:
            snake.grow()
            move_fruit()

        # check for collision with tail or border

        pygame.display.update()

        snake.step()
        clock.tick(10)


main()
