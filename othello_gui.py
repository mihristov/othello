import pygame
import sys

from othello_game import Game

pygame.init()

SIZE = 50
BORDER = 1
PADDING = 20
DIMENSION = SIZE * 8 + BORDER * 10
THICKNESS = 20

WHITE = (255, 255, 255)
GREEN = (0,   210,   11)
BLACK = (0, 0, 0)

OVERLAY_ALPHA = 180
game = Game()
pygame.display.set_caption('Othello')
screen = pygame.display.set_mode([DIMENSION, DIMENSION])
font = pygame.font.SysFont("monospace", 33, True)


def square_to_rectangle(square):
    row = square // 8
    column = square % 8

    x = BORDER + (SIZE + BORDER) * row
    y = BORDER + (SIZE + BORDER) * column
    return [x, y, SIZE, SIZE]


def square_to_inner_rectangle(square):
    x, y, w, h = square_to_rectangle(square)

    x += PADDING
    y += PADDING
    w -= PADDING * 2
    h -= PADDING * 2

    return [x, y, w, h]


def draw_white(square):
    x, y, w, h = square_to_inner_rectangle(square)

    pygame.draw.ellipse(
        screen, WHITE, [x - 15, y - 15, w + 30, h + 30], THICKNESS)


def draw_black(square):
    x, y, w, h = square_to_inner_rectangle(square)

    pygame.draw.ellipse(
        screen, BLACK, [x - 15, y - 15, w + 30, h + 30], THICKNESS)


def within(point, rectangle):
    x, y = point
    l, t, w, h = rectangle

    return l <= x <= l + w and t <= y <= t + h


def square_for(position):
    for i in range(64):
        rectangle = square_to_rectangle(i)
        if within(position, rectangle):
            return i

    return None


def draw_board():
    screen.fill(BLACK)

    for i in range(64):
        rectangle = square_to_rectangle(i)
        pygame.draw.rect(screen, GREEN, rectangle)

    for i in range(64):
        if game.at(i) == Game.WHITE:
            draw_white(i)
        elif game.at(i) == Game.BLACK:
            draw_black(i)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            square = square_for(position)
            game.play(square)

    draw_board()
    pygame.display.flip()
