import pygame
import time
from sys import exit

#Initialisation
pygame.init()
screen = pygame.display.set_mode((750 , 800))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
GREEN = ( 0 , 255, 0)
RED = (255, 0, 0)
TEMP = (210, 0, 210)
BLACK = (0, 0, 0)

def is_valid_move(matrix, x, y):    #if the move made is within bounds
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != 0

def is_junction(valid_moves):
    return len(valid_moves) >= 3

def mark_entrance(matrix, x, y):        #marks entrance of a path based on it's previous marking value
    if matrix[x][y] == 1:
        matrix[x][y] = 2
        return True
    elif matrix[x][y] == 2:
        matrix[x][y] = 3
        return True
    
    return False

def dead_end(valid_moves):
    return len(valid_moves) == 1

def blit_grid(matrix):
    for i in range(len(matrix)):

        for j in range(len(matrix[0])):
            if matrix[j][i] == 0:
                pygame.draw.rect(maze_surface ,BLUE , ( 1 + 30*i ,1 + 30*j ,30, 30 ) ,4)
            elif matrix[j][i] == 1:
                pygame.draw.rect(maze_surface , BLACK , ( 1 + 30*i ,1 + 30*j ,30, 30 ) ,4)
            # elif matrix[j][i] == 2:
            #     pygame.draw.rect(maze_surface ,GREEN , ( 1 + 30*i ,1 + 30*j ,30, 30 ) ,4)
            # elif matrix[j][i] == 3:
            #     pygame.draw.rect(maze_surface ,RED , ( 1 + 30*i ,1 + 30*j ,30 , 30 ) ,4)

def tremaux(matrix):

    x,y, prev_x, prev_y  = 1, 1, 0, 0

    mark_entrance(matrix , x, y)

    length = len(matrix)

    while not(x == length - 2 and y == length - 2):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #adding surfaces
        screen.blit(background , (0,0)) 
        screen.blit(maze_surface , (50 , 50))

        pygame.display.update()
        clock.tick(60)

        valid_moves = [( x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if is_valid_move(matrix, x + dx, y + dy)]# all possible movements available regardless of marking

        if is_junction(valid_moves):

            flag = False #to check if we found a way
            mark_entrance(matrix ,prev_x , prev_y) # mark the entrance u r leaving
            
            for i in valid_moves: #checking unmarked entrances

                possible_x, possible_y = i
                if matrix[possible_x][possible_y] == 1:
                    next_x, next_y = possible_x, possible_y 
                    prev_x, prev_y = x, y
                    mark_entrance(matrix, next_x , next_y)       
                    flag = True
                    break

            if (not flag and matrix[prev_x][prev_y] != 3): #go back the current path if not marked twice
                next_x, next_y = prev_x, prev_y
                prev_x, prev_y = x, y
                mark_entrance(matrix, prev_x , prev_y)

            if ( not flag ):    #else pick any entrance marked once
                for i in valid_moves:  
                    if matrix[i[0]][i[1]] == 2:
                        next_x, next_y = i[0], i[1]
                        mark_entrance(matrix, next_x, next_y)
                        prev_x, prev_y = x, y
                        break

        else:                   # otherwise it's a normal path continue as needed
            if dead_end(valid_moves):
                mark_entrance(matrix, x, y)
                mark_entrance(matrix, x, y)
                prev_x, prev_y = x, y
                next_x, next_y = valid_moves[0][0], valid_moves[0][1]

            elif ( len(valid_moves) >= 2 ):
                if ( prev_x, prev_y ) in valid_moves:
                    valid_moves.remove((prev_x, prev_y))
                prev_x, prev_y = x, y
                next_x, next_y = valid_moves[0][0], valid_moves[0][1]
              
        x, y = next_x, next_y
        pygame.draw.rect(maze_surface , TEMP , ( 1 + 30 * x ,1 + 30 * y ,30 ,30 ) ,4)

        blit_grid(matrix)

def dfs_with_path(maze, start, goal):
    
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    rows, cols = len(maze), len(maze[0])
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1 

    def dfs_search(x, y, path):
        maze[x][y] = 2

        if (x, y) == goal:
            path.append((x, y))
            return True

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                if dfs_search(new_x, new_y, path):
                    path.append((x, y))  
                    return True

        return False

    path = []
    if dfs_search(start[0], start[1], path):
        for x, y in path:
            maze[x][y] = 3
        return path[::-1] 
    return None  

# main surfaces for the display

background = pygame.Surface((750, 700))
background.fill("White")

maze_surface = pygame.Surface((604,604))

#variables
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
#graphics functions
# print(matrix)
path = dfs_with_path(matrix , (1, 1), ( len(matrix) - 2 , len(matrix) - 2))
print(path)
# tremaux(matrix)

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #adding surfaces
    screen.blit(background , (0,0)) 
    screen.blit(maze_surface , (50 , 50))
    blit_grid(matrix)
    for (i, j) in path:
        pygame.draw.rect(maze_surface ,TEMP , ( 10 + 30*j , 10 + 30*i ,15, 15 ) ,5)
    pygame.display.update()
    clock.tick(60)
