import random
import pygame
import time
from sys import exit

directions = {'forward':'N','left':'W','back':'S','right':'E'} #standard directions

pygame.init()
WIDTH, HEIGHT = 20, 20

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

grid = [[ Cell() for i in range( WIDTH )] for i in range( HEIGHT ) ]

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


def rotate_clockwise():
    keys = directions.keys()
    values = directions.values()
    values = values[1:] + values[0]
    directions = dict( zip(keys , values) )

def rotate_anti_clockwise():
    keys = directions.keys()
    values = directions.values()
    values = values[-1] + values[:2]
    directions = dict( zip(keys , values) )

def moveForward(x, y):

    if directions['forward']=='E':
        return ( x, y + 1 )
    if directions['forward']=='W':
        return (x,y-1)
    if directions['forward']=='N':
        return ( x - 1, y )
    if directions['forward']=='S':
        return ( x + 1 , y)

x, y = 0, 0
while not( x == WIDTH - 1 and y == HEIGHT - 1 ) :
    #checking left wall
    if directions['left']=='E':
        if grid[x][y].E == 0:
            #checking front wall
            if directions['forward']=='E':
                if grid[x][y].E == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
            elif directions['forward']=='W':
                if grid[x][y].W == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
                
            elif directions['forward']=='N':
                if grid[x][y].N == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)    
            elif directions['forward']=='S':
                if grid[x][y].S == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)  
        else:
            rotate_anti_clockwise()
            x, y = moveForward(x, y)               
    
    elif directions['left']=='N':
        if grid[x][y].N == 0:
            #checking front wall
            if directions['forward']=='E':
                if grid[x][y].E == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
            elif directions['forward']=='W':
                if grid[x][y].W == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
                
            elif directions['forward']=='N':
                if grid[x][y].N == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)    
            elif directions['forward']=='S':
                if grid[x][y].S == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)  
        else:
            rotate_anti_clockwise()
            x, y = moveForward(x, y)  
        
    elif directions['left']=='W':
        if grid[x][y].W == 0:
            #checking front wall
            if directions['forward']=='E':
                if grid[x][y].E == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
            elif directions['forward']=='W':
                if grid[x][y].W == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
                
            elif directions['forward']=='N':
                if grid[x][y].N == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)    
            elif directions['forward']=='S':
                if grid[x][y].S == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)  
        else:
            rotate_anti_clockwise()
            x, y = moveForward(x, y)  

    elif directions['left']=='S':
        if grid[x][y].S == 0:
            #checking front wall
            if directions['forward']=='E':
                if grid[x][y].E == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
            elif directions['forward']=='W':
                if grid[x][y].W == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)
                
            elif directions['forward']=='N':
                if grid[x][y].N == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)    
            elif directions['forward']=='S':
                if grid[x][y].S == 0:
                    forward_block_flag = True
                    rotate_clockwise()
                else:
                    x, y = moveForward(x, y)  
        else:
            rotate_anti_clockwise()
            x, y = moveForward(x, y)  


