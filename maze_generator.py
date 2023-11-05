import cmath
import random
import pygame
import time
from sys import exit

pygame.init()
width, height = 20, 20
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 750
wall_thickness = 2
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

maze_surface = pygame.Surface( (750, 750) )
maze_surface.fill((0,0,0))
maze_rect = maze_surface.get_rect(topleft = (0, 0))

control_surface = pygame.Surface((750, 750))
control_surface.fill((255, 255, 255))
control_rect = control_surface.get_rect(topleft = (750, 0))

# Colours
CELL_SIZE = 35
SMALL_BLOCK_SIZE = 10
WALL_COLOR = (0, 0, 0)  # Black
PATH_COLOR = (0, 0, 0)  # White
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TEMP = (210, 0, 210)

class Button:
    def __init__(self, x, y, width, height, text, color):
        font = pygame.font.Font(None, 20)
        self.text = font.render("This is a button", True, color)
        self.text_rect = self.text.get_rect(center = (x, y) )
    def draw(self):
        pygame.draw.rect(screen, TEMP, self.text_rect)  


b1 = Button(750 ,0 , 500, 500, "This is a button", BLUE )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    screen.fill((0, 0 , 0))
    screen.blit(control_surface, control_rect)
    screen.blit(maze_surface, maze_rect)
    b1.draw()
    #draw_maze(grid)
    pygame.display.update()
    clock.tick(30)
