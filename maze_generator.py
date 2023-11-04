import cmath
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
directions = {'forward':'N','left':'W','back':'S','right':'E'} #standard directions

# Colours
CELL_SIZE = 35
SMALL_BLOCK_SIZE = 10
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
        self.visited = False

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

def draw_maze(grid):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, (0, 0, CELL_SIZE-5, CELL_SIZE-5))
    pygame.draw.rect(screen, GREEN, ((width-1)* CELL_SIZE, (height-1)* CELL_SIZE, CELL_SIZE-5, CELL_SIZE-5))
    for y in range(height):
        for x in range(width):
            cell = grid[y][x]

            cell_x = x * CELL_SIZE
            cell_y = y * CELL_SIZE

            if cell.N == 0:
                pygame.draw.rect(screen, BLUE, (cell_y, cell_x, CELL_SIZE, wall_thickness))
            if cell.W == 0:
                pygame.draw.rect(screen, BLUE, (cell_y, cell_x, wall_thickness, CELL_SIZE))

    pygame.draw.rect(screen, BLUE, (0, height*CELL_SIZE, width*CELL_SIZE, wall_thickness))
    pygame.draw.rect(screen, BLUE, (width * CELL_SIZE, 0, wall_thickness, CELL_SIZE*width))
    pygame.display.update()

def make_borders(grid):
    #top border:
    for i in grid[0]:
        i.N = 0
    #bottom border
    for i in grid[height - 1]:
        i.S = 0
    #left border
    for i in range(height):
        grid[i][0].W = 0
    #right border
    for i in range(height):
        grid[i][width - 1].E = 0

grid = [[Cell() for i in range(width)] for i in range(height)]

def choose_random_adjacent(x,y):

    directions= ['N','E','S','W']

    while True:
        if len(directions) == 0:
            return -999, -999
        try:
            rand_index = random.randint(0, len(directions)-1)
        except ValueError:
            print(directions)
            print("-----------------------help------------------------")
        random_direction = directions[rand_index]

        # print(random_direction, directions)

        if (random_direction == 'N'):
            if ( (x, y - 1) in visited or (x, y - 1) in visited_with_visited_neigh or not(check_bounds(x,y-1))):
                directions.remove('N')
            else:
                # print("in n else", x,y-1)
                grid[x][y].carve_north(grid[x][y-1])
                return x, y - 1
        elif (random_direction == 'E'):
            if ( (x+1, y ) in visited or (x+1, y) in visited_with_visited_neigh or not(check_bounds(x+1,y))):
                directions.remove('E')
            else:
                # print("in east else",x+1,y)
                grid[x][y].carve_east(grid[x+1][y])
                return x + 1,y

        elif (random_direction == 'S'):
            if ( (x, y +1) in visited or (x, y + 1) in visited_with_visited_neigh or  not(check_bounds(x,y+1))):
                directions.remove('S')
            else:
                grid[x][y].carve_south(grid[x][y+1])
                return x, y + 1

        elif (random_direction == 'W'):
            if ( (x-1, y) in visited or (x-1, y ) in visited_with_visited_neigh or  not(check_bounds(x-1,y))):
                directions.remove('W')
            else:
                # print("in w else", x-1,y)
                grid[x][y].carve_west(grid[x - 1][y])
                return x-1 ,y

# initialising list
visited = []
visited_with_visited_neigh= []
x= random.randint(0,width-1)
y= random.randint(0,height-1)
visited.append((x,y))

while visited:
    # print(visited)
    # print(visited_with_visited_neigh)
    x,y = visited[-1]
    x1,y1 = choose_random_adjacent(x,y)
    # print("X1 AND Y1=",x1, y1)
    if x1 < 0 and y1 < 0:
        # print("in negative")
        visited.remove((x,y))
        visited_with_visited_neigh.append((x,y))
        # print(visited)
        # print(visited_with_visited_neigh)
    else:
        visited.append((x1,y1))

    draw_maze(grid)
    pygame.time.delay(5)

def rotate_clockwise():
    global directions
    keys = list(directions.keys())
    v = list(directions.values())
    v_rotated=[v[-1]]+v[:-1]
    directions = dict(zip(keys,v_rotated))

def rotate_anti_clockwise():
    global directions
    keys = list(directions.keys())
    v = list(directions.values())
    v_rotated=v[1:]+[v[0]]
    directions = dict(zip(keys,v_rotated))

def moveForward(x, y):
    global directions
    if directions['forward']=='E':
        return x, y + 1
    if directions['forward']=='W':
        return x,y-1
    if directions['forward']=='N':
        return x - 1, y
    if directions['forward']=='S':
        return x + 1 , y

# def draw_path(x, y):
#     #figuring out where left wall is
#     if directions['left'] == "N":




#     cell_x = x * CELL_SIZE
#     cell_y = y * CELL_SIZE
#     pygame.display.update()


x, y = 0, 0
while not( x == width - 1 and y == height - 1 ) :
    #checking left wall
    if directions['left']=='E':
        if grid[y][x].E == 0:
            #checking front wall
            if directions['forward']=='E':
                if grid[y][x].E == 0:
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
            elif directions['forward']=='W':
                if grid[y][x].W == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
                
            elif directions['forward']=='N':
                if grid[y][x].N == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)    
            elif directions['forward']=='S':
                if grid[y][x].S == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)  
        else:
            rotate_anti_clockwise()
            x, y = moveForward(x, y)               
    
    elif directions['left']=='N':
        if grid[y][x].N == 0:
            #checking front wall
            if directions['forward']=='E':
                if grid[y][x].E == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
            elif directions['forward']=='W':
                if grid[y][x].W == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
                
            elif directions['forward']=='N':
                if grid[y][x].N == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)    
            elif directions['forward']=='S':
                if grid[y][x].S == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)  
        else:
            rotate_anti_clockwise()
            x, y = moveForward(x, y)  
        
    elif directions['left']=='W':
        if grid[y][x].W == 0:
            #checking front wall
            if directions['forward']=='E':
                if grid[y][x].E == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
            elif directions['forward']=='W':
                if grid[y][x].W == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
                
            elif directions['forward']=='N':
                if grid[y][x].N == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)    
            elif directions['forward']=='S':
                if grid[y][x].S == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)  
        else:
            rotate_anti_clockwise()
            x, y = moveForward(x, y)  

    elif directions['left']=='S':
        if grid[y][x].S == 0:
            #checking front wall
            if directions['forward']=='E':
                if grid[y][x].E == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
            elif directions['forward']=='W':
                if grid[y][x].W == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
                
            elif directions['forward']=='N':
                if grid[y][x].N == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)    
            elif directions['forward']=='S':
                if grid[y][x].S == 0:
                    
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)  
        else:
            rotate_anti_clockwise()
            x, y = moveForward(x, y)  
    draw_maze(grid)
    pygame.draw.rect(screen, TEMP, (y* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, x* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
    pygame.display.update()    
    pygame.time.delay(40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    #draw_maze(grid)
    pygame.display.update()
    clock.tick(30)
