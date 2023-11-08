import random
import pygame
import time
from sys import exit
import binary_tree

pygame.init()
width, height = 20, 20
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 750
wall_thickness = 2
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()
directions = {'forward':'N','left':'W','back':'S','right':'E'} #standard directions


# Colours
CELL_SIZE = 35
SMALL_BLOCK_SIZE = 10
BLACK = WALL_COLOR = (0, 0, 0)  # Black
WHITE = PATH_COLOR = (0, 0, 0)  # White
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TEMP = (210, 0, 210)

maze_surface = pygame.Surface( (750, 750) )
maze_surface.fill((0,0,0))
maze_rect = maze_surface.get_rect(topleft = (0, 0))

control_surface = pygame.Surface((750, 750))
control_surface.fill((255, 255, 255))
control_rect = control_surface.get_rect(topleft = (750, 0))

class Button:
    def __init__(self, x, y, width, height, text, color, action = None):
        self.rect = pygame.Rect(x, y, width, height)
        font = pygame.font.Font(None, 30)
        self.text = font.render(text, False, color)
        self.text_rect = self.text.get_rect(center = self.rect.center )
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, BLUE ,self.rect, 4, 10) 
        screen.blit(self.text, self.text_rect)

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

grid = [[Cell() for i in range(width)] for i in range(height)]

def draw_maze(grid):
    screen.blit(maze_surface, maze_rect)
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

def binary_tree():
    # initialising list
    visited = []
    visited_with_visited_neigh= []
    x= random.randint(0,width-1)
    y= random.randint(0,height-1)
    visited.append((x,y))

    def check_bounds(nx, ny):
        return ny < height and ny >= 0  and nx < width and nx >=0
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
        screen.blit(control_surface, control_rect)
        screen.blit(maze_surface, maze_rect)
        draw_maze(grid)

        b1.draw()
        b2.draw()
        b3.draw()
        b4.draw()
        text_1.draw()
        text_2.draw()
        pygame.display.update()
        clock.tick(100)

def left_wall_follower():
    
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

    def draw_path(x, y):
        cell_x = x * CELL_SIZE
        cell_y = y * CELL_SIZE

        #figuring out where left wall is
        if directions['left'] == "N":
            pygame.draw.rect(screen, GREEN , (cell_y, cell_x,CELL_SIZE,wall_thickness))
        if directions['left'] == "S":
            pygame.draw.rect(screen, GREEN , (cell_y, cell_x,CELL_SIZE,wall_thickness))
        if directions['left'] == "E":
            pygame.draw.rect(screen, GREEN , (cell_y, cell_x,wall_thickness,CELL_SIZE))
        if directions['left'] == "W":
            pygame.draw.rect(screen, GREEN , (cell_y, cell_x,wall_thickness,CELL_SIZE))


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
        draw_path(x, y)
        # screen.blit(control_surface, control_rect)
        b1.draw()
        b2.draw()
        b3.draw()
        b4.draw()
        text_1.draw()
        text_2.draw()

        pygame.display.update()    
        clock.tick(30)

def dikshtra():
    def draw_path(path):
        for i in path:
            pygame.draw.rect(screen, TEMP, (i[1]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, i[0]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
            pygame.display.update()
    def min_cell():
        min, min_index = 1000000,(0,0)
        for i in unvisited:
            if unvisited[i] < min:
                min = unvisited[i]
                min_index = i
        return min_index        

    unvisited, visited,path = {}, [], []
    #setting all the values in unvisited to infinity
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            unvisited[(i, j)] = 10000
    unvisited[(0, 0)] = 0

    while unvisited:
        currcell = min_cell()
        visited.append(currcell)

        if currcell == (len(grid) - 1, len(grid [0]) - 1):
            break

        for i in "NEWS":

            if grid[currcell[0]][currcell[1]] == 1:
                
                if i=='E':
                    childCell = (currCell[0],currCell[1]+1)
                elif i=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif i=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif i=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                temp_dist = unvisited[currcell] + 1
                if temp_dist < unvisited[childCell]:
                    unvisited[childCell] = temp_dist
                    path.append(currcell)

        unvisited.pop(currcell)
    draw_path(path)

b1 = Button(800 ,100 , 120, 50, "Binary Tree", BLACK, action = binary_tree)
b2 = Button(1300 ,100 , 120, 50, "DFS", BLACK)
b3 = Button(800 ,500 , 180, 50, "Left wall follower", BLACK, action = left_wall_follower)
b4 = Button(1300 ,500 , 120, 50, "Dikshtra", BLACK, action= dikshtra)

text_1 = Button(950, 10, 300, 50, "Maze Generation Algorithms", BLACK)
text_2 = Button(950, 400, 300, 50, "Maze Solving Algorithms", BLACK)

screen.fill((0, 0 , 0))

if __name__=='__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if b1.rect.collidepoint(event.pos):
                        b1.action()
                    elif b2.rect.collidepoint(event.pos):
                        b2.action()
                    elif b3.rect.collidepoint(event.pos):
                        b3.action()
                    elif b4.rect.collidepoint(event.pos):
                        b4.action()        

        screen.blit(control_surface, control_rect)
        screen.blit(maze_surface, maze_rect)
        draw_maze(grid)

        b1.draw()
        b2.draw()
        b3.draw()
        b4.draw()
        text_1.draw()
        text_2.draw()
        pygame.display.update()
        clock.tick(60)
