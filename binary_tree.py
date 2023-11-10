import random
import pygame
import time
from sys import exit

pygame.init()
width, height = 20, 20
SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
wall_thickness = 2
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

#Colours
CELL_SIZE = 35 
WALL_COLOR = (0, 0, 0)  # Black
PATH_COLOR = (0, 0, 0)  # White
BLUE = (0, 0, 255)
GREEN = ( 0 , 255, 0)
RED = (255, 0, 0)
TEMP = (210, 0, 210)

#Filling the surfaces with colours
# background = pygame.Surface((800, 800))
# background.fill("White")
# maze_surface = pygame.Surface((800,800))
# maze_surface.fill("White")


class Cell:
    def __init__(self): #in directions 1 represents open path and 0 closed path
        self.N = 0
        self.W = 0
        self.E = 0
        self.S = 0
    def carve_north(self, cell):
        self.N = 1 #carving in the north direction
        cell.S = 1 # for the upper cell the opposite direction will be taken
    def carve_west(self, cell):
        self.W = 1 #carving in the north direction
        cell.E = 1 # for the upper cell the opposite direction will be taken    

def check_bounds(nx, ny):
    return ny < height and nx < width

#directions
N, S, E, W = 1, 2, 4, 8
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}

grid = [[ Cell() for i in range(width)] for i in range(height)]

# Function to draw the maze
def draw_maze(grid):
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, RED, (0, 0, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (19* CELL_SIZE, 19* CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for y in range(height):
        for x in range(width):
            cell = grid[y][x]

            cell_x = x * CELL_SIZE
            cell_y = y * CELL_SIZE

            if cell.N == 0:
                pygame.draw.rect(screen, BLUE, (cell_x, cell_y, CELL_SIZE, wall_thickness))
            if cell.W == 0:
                pygame.draw.rect(screen, BLUE, (cell_x, cell_y, wall_thickness, CELL_SIZE))
            if cell.E == 0:
                pygame.draw.rect(screen, BLUE, (cell_x + CELL_SIZE - wall_thickness, cell_y, wall_thickness, CELL_SIZE))
            if cell.S == 0:
                pygame.draw.rect(screen, BLUE, (cell_x, cell_y + CELL_SIZE - wall_thickness, CELL_SIZE, wall_thickness))
            if cell.N == 1 and cell.W == 1 and cell.E == 1 and cell.S == 1:
                pygame.draw.rect(screen, PATH_COLOR, (cell_x, cell_y, CELL_SIZE, CELL_SIZE))
    pygame.display.update()          



dirs = [N, W]                               #possible directions for movement
for y in range(height):                     #rows
    for x in range(width):                  #columns
        dir = random.choice(dirs)           #pick random diresction for movement
        nx, ny = x + DX[dir], y + DY[dir]   #new x and y
        if check_bounds( nx, ny):
            if dir == N:
                (grid[y][x]).carve_north(grid[ny][nx])
            elif dir == W:
                (grid[y][x]).carve_west(grid[ny][nx])
        draw_maze( grid ) 
        pygame.time.delay(10) 

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    
    # Call the draw_maze function to draw the maze on the screen
    draw_maze(grid)
    # Update the display
    pygame.display.update()   
    clock.tick(30)   