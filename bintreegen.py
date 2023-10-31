import cmath
import random
import pygame
import time
from sys import exit

pygame.init()
width, height = 3, 3
SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
wall_thickness = 2
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

# Colours
CELL_SIZE = 35
WALL_COLOR = (0, 0, 0)  # Black
PATH_COLOR = (0, 0, 0)  # White
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TEMP = (210, 0, 210)


class Cell:
    def __init__(self):  # in directions 1 represents open path and 0 closed path
        self.N = 0
        self.W = 0
        self.E = 0
        self.S = 0

    def carve_north(self, cell):
        self.N = 1  # carving in the north direction
        cell.S = 1  # for the upper cell the opposite direction will be taken

    def carve_east(self, cell):
        self.E = 1  # carving in the north direction
        cell.W = 1  # for the upper cell the opposite direction will be taken

    def carve_south(self, cell):
        self.S = 1  # carving in the north direction
        cell.N = 1  # for the upper cell the opposite direction will be taken

    def carve_west(self, cell):
        self.W = 1  # carving in the north direction
        cell.E = 1  # for the upper cell the opposite direction will be taken


def check_bounds(nx, ny):
    return ny < height and ny >= 0  and nx < width and nx >=0


# Function to draw the maze
def draw_maze(grid):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, (0, 0, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (19 * CELL_SIZE, 19 * CELL_SIZE, CELL_SIZE, CELL_SIZE))
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
                pygame.draw.rect(screen, BLUE,
                                 (cell_x + CELL_SIZE - wall_thickness, cell_y, wall_thickness, CELL_SIZE))
            if cell.S == 0:
                pygame.draw.rect(screen, BLUE,
                                 (cell_x, cell_y + CELL_SIZE - wall_thickness, CELL_SIZE, wall_thickness))
            if cell.N == 1 and cell.W == 1 and cell.E == 1 and cell.S == 1:
                pygame.draw.rect(screen, PATH_COLOR, (cell_x, cell_y, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

grid = [[Cell() for i in range(width)] for i in range(height)]


def choose_random_adjacent(x,y):

    directions= ['N','E','S','W']
    if (len(directions)==0):
        return (-999, -999)
    else:
        not_returned= True
        while(not_returned):
            rand_index = random.randint(0, len(directions)-1)
            random_direction = directions[rand_index]

            print(random_direction, directions)

            if (random_direction == 'N'):
                if ( (x, y - 1) in visited or (x, y - 1) in visited_with_visited_neigh or not(check_bounds(x,y-1))):
                    directions.remove('N')
                else:
                    print("in n else", x,y-1)
                    grid[x][y].carve_north(grid[x][y-1])
                    not_returned = False
                    return x, y - 1
            elif (random_direction == 'E'):
                if ( (x+1, y ) in visited or (x+1, y) in visited_with_visited_neigh or not(check_bounds(x+1,y))):
                    directions.remove('E')
                else:
                    print("in east else",x+1,y)
                    grid[x][y].carve_east(grid[x+1][y])
                    not_returned = False
                    return x + 1,y

            elif (random_direction == 'S'):
                if ( (x, y +1) in visited or (x, y + 1) in visited_with_visited_neigh or  not(check_bounds(x,y+1))):
                    directions.remove('S')
                else:
                    grid[x][y].carve_south(grid[x][y+1])
                    not_returned = False
                    return x, y + 1

            elif (random_direction == 'W'):
                if ( (x-1, y) in visited or (x-1, y ) in visited_with_visited_neigh or  not(check_bounds(x-1,y))):
                    directions.remove('W')
                else:
                    print("in w else", x-1,y)
                    grid[x][y].carve_west(grid[x - 1][y])
                    not_returned = False
                    return x-1 ,y

# setting grid dimensions
# Max_length = 5
# Max_width = 5

# initialising list
visited = []
visited_with_visited_neigh= []
x= random.randint(0,width-1)
y= random.randint(0,height-1)

visited.append((x,y))

while visited:
    print(visited)
    print(visited_with_visited_neigh)
    x,y = visited[-1]
    x1,y1 = choose_random_adjacent(x,y)
    print("X1 AND Y1=",x1, y1)
    if x1 < 0 and y1 < 0:
        visited.remove((x,y))
        visited_with_visited_neigh.append((x,y))
    else:
        visited.append((x1,y1))

    # draw_maze(grid)
    # pygame.time.delay(10)



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
