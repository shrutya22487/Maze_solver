import random
import pygame
import time
from sys import exit
# import binary_tree

pygame.init()
width, height = 20, 20
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 750
wall_thickness = 3
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()
directions = {'forward':'N','left':'W','back':'S','right':'E'} #standard directions


# Colours
CELL_SIZE = 37
SMALL_BLOCK_SIZE = 10
BLACK = WALL_COLOR = (0, 0, 0)  # Black
WHITE = PATH_COLOR = (255, 255, 255)  # White
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
    def __init__(self, x, y, width, height, text, color, Border_thickness,Border_color, action = None):
        self.rect = pygame.Rect(x, y, width, height)
        font = pygame.font.Font(None, 30)
        self.text = font.render(text, False, color)
        self.text_rect = self.text.get_rect(center = self.rect.center )
        self.action = action
        self.border_thickness = Border_thickness
        self.border_color = Border_color

    def draw(self):
        pygame.draw.rect(screen, self.border_color ,self.rect, self.border_thickness, 10) 
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

#Grid manipulation
def fiveXfive():
    global clock_tick
    clock_tick = 30
    global wall_thickness
    wall_thickness = 8
    global width 
    width = 5
    global height
    height = 5
    global CELL_SIZE
    CELL_SIZE = 140
    global SMALL_BLOCK_SIZE
    SMALL_BLOCK_SIZE = 60

def tenXten():
    global clock_tick
    clock_tick = 60
    global wall_thickness
    wall_thickness = 6
    global width 
    width = 10
    global height
    height = 10
    global CELL_SIZE
    CELL_SIZE = 70
    global SMALL_BLOCK_SIZE
    SMALL_BLOCK_SIZE = 30

def twentyXtwenty():
    global clock_tick
    clock_tick = 120
    global wall_thickness
    wall_thickness = 4
    global width 
    width = 20
    global height
    height = 20
    global CELL_SIZE
    CELL_SIZE = 37
    global SMALL_BLOCK_SIZE
    SMALL_BLOCK_SIZE = 10    

def reset():
    global grid
    grid = [[Cell() for i in range(width)] for i in range(height)]


def draw_maze(grid):
    screen.blit(maze_surface, maze_rect)
    pygame.draw.rect(screen, RED, (0, 0, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, ((width-1)* CELL_SIZE, (height-1)* CELL_SIZE, CELL_SIZE, CELL_SIZE))
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

def check_bounds(nx, ny):
        return ny < height and ny >= 0  and nx < width and nx >=0


def binary_tree():
    # initialising list
    visited = []
    visited_with_visited_neigh= []
    x= random.randint(0,width-1)
    y= random.randint(0,height-1)
    visited.append((x,y))

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
        draw_nodes()
        pygame.display.update()
        clock.tick(200)

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
        draw_nodes()

        pygame.display.update()    
        clock.tick(30)

def prims_algorithm():
    frontier = []  # List to store frontier
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)  #random cell to start
    visited = set((start_x, start_y))  # Set to store visited cells

    # Function to add neighboring walls to the list
    def add_frontier(x, y):
        if check_bounds(x - 1, y) and (x - 1, y) not in visited:
            frontier.append(((x, y), 'N', (x - 1, y)))
        if check_bounds(x + 1, y) and (x + 1, y) not in visited:
            frontier.append(((x, y), 'S', (x + 1, y)))
        if check_bounds(x, y - 1) and (x, y - 1) not in visited:
            frontier.append(((x, y), 'W', (x, y - 1)))
        if check_bounds(x, y + 1) and (x, y + 1) not in visited:
            frontier.append(((x, y), 'E', (x, y + 1)))

    add_frontier(start_x, start_y)         # add frontier

    while frontier:       # selecting random frotier
        frontier_index = random.randint(0, len(frontier) - 1)
        current_cell, direction, neighbor = frontier.pop(frontier_index)     # choose a rando frontier

        current_x, current_y = current_cell
        neighbor_x, neighbor_y = neighbor

        if neighbor not in visited: # selecting random frotier of new frontier
            visited.add(neighbor)

            # Carve path from chosen cell and frontier
            if direction == 'N':
                grid[current_y][current_x].carve_north(grid[neighbor_y][neighbor_x])
            elif direction == 'S':
                grid[current_y][current_x].carve_south(grid[neighbor_y][neighbor_x])
            elif direction == 'W':
                grid[current_y][current_x].carve_west(grid[neighbor_y][neighbor_x])
            elif direction == 'E':
                grid[current_y][current_x].carve_east(grid[neighbor_y][neighbor_x])

            # Add neighboring walls of the visited cell
            add_frontier(neighbor_x, neighbor_y)         #mark neighbour of frontier as frontier

        draw_maze(grid)
        pygame.display.update()
        clock.tick(60)

def dikshtra():

    def draw_path(path):
        for i in path:
            pygame.draw.rect(screen, TEMP, (i[0]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, i[1]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
            pygame.time.delay(100)
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

    def min_cell():
        min, min_index = 1000000,(0,0)
        for i in unvisited:
            if unvisited[i] < min:
                min = unvisited[i]
                min_index = i
        return min_index        

    def set_all_to_infinity():
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                unvisited[(i, j)] = 10000
    
    unvisited,revpath, visited = {}, {} , []
    #setting all the values in unvisited to infinity
    set_all_to_infinity()
    currcell = (len(grid) - 1, len(grid[0]) - 1 )
    unvisited[currcell] = 0

    # make_borders(grid)

    while unvisited:
        currcell = min_cell()

        # pygame.draw.rect(screen, TEMP, (currcell[1]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, currcell[0]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
        # pygame.display.update()
        visited.append(currcell)

        if currcell == (0, 0):
            break

        for i in "NEWS":
            childCell = 0
            if i == "E" and grid[currcell[0]][currcell[1]].E == 1:
                childCell = (currcell[0] + 1,currcell[1])

            elif i == "W" and grid[currcell[0]][currcell[1]].W == 1:
                childCell=(currcell[0] - 1,currcell[1])

            elif i == "S" and grid[currcell[0]][currcell[1]].S == 1:
                childCell=(currcell[0] ,currcell[1] + 1)

            elif i == "N" and grid[currcell[0]][currcell[1]].N == 1:
                childCell=(currcell[0],currcell[1] - 1)

            if childCell != 0 and childCell in visited:
                continue

            temp_dist = unvisited[currcell] + 1

            if childCell != 0 and temp_dist < unvisited[childCell]:
                unvisited[childCell] = temp_dist
                revpath[childCell] = currcell

        unvisited.pop(currcell)
    fwdpath = {}
    cell = (0,0)
    while cell != (len(grid) - 1, len(grid[0]) - 1):
        fwdpath[revpath[cell]] = cell
        cell = revpath[cell]

    draw_path( fwdpath )
    print(revpath)
    pygame.time.delay(5000)
def dfs1():
    def get_unvisited_neighbors(x, y):
        neighbours =[]
        if grid[y][x].N ==1 and (x-1,y) not in visited:
            neighbours.append((x-1,y))
            # visited.add((x-1,y))
        if grid[y][x].E ==1 and (x,y+1) not in visited:
            neighbours.append((x,y+1))
            # visited.add((x, y+1))
        if grid[y][x].S ==1 and (x+1,y) not in visited:
            neighbours.append((x+1,y))
            # visited.add((x + 1, y))
        if grid[y][x].W ==1 and (x,y-1) not in visited:
            neighbours.append((x,y-1))
            # visited.add((x, y - 1))

        return neighbours

    stack = [(0, 0)]  # Starting position
    visited = set()

    while stack:
        x, y = stack[-1]
        visited.add((x,y))

        if (x, y) == (width - 1, height - 1):  # Reached the exit
            print("DFS Path Found!")
            draw_solution_path((x, y), visited)
            pygame.time.delay(5000)
            return

        temp = get_unvisited_neighbors(x, y)
        if len(temp)==0:
            stack.remove((x,y))
        else:
            stack.extend(temp)
            #print(stack)

        draw_maze(grid)
        draw_solution_path((x, y), visited)
        draw_nodes()

        pygame.display.update()
        clock.tick(20)

    print("DFS: No Path Found!")



def draw_solution_path(cell, visited):
    for x, y in visited:
        pygame.draw.rect(screen, TEMP, (y * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                        x * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                        SMALL_BLOCK_SIZE))
    pygame.draw.rect(screen, TEMP, (cell[1] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                    cell[0] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                    SMALL_BLOCK_SIZE))

b1 = Button(800 ,100 , 120, 50, "Binary Tree", BLACK, 4,BLUE,  action = binary_tree)
b2 = Button(1300 ,100 , 120, 50, "Prims algo", BLACK,4, BLUE, action = prims_algorithm)
b3 = Button(800 ,300 , 180, 50, "Left wall follower", BLACK,4, BLUE, action = left_wall_follower)
b4 = Button(1300 ,300 , 120, 50, "Dikshtra", BLACK,4, BLUE, action= dikshtra)
b5 = Button(800, 500, 120, 50, "5 X 5" ,BLACK, 4, BLUE, action = fiveXfive)
b6 = Button(1050, 500, 120, 50, "10 X 10" ,BLACK, 4, BLUE, action = tenXten)
b7 = Button(1300, 500, 120, 50, "20 X 20" ,BLACK, 4, BLUE, action = twentyXtwenty)
b8 = Button(1050, 700, 120, 50, "RESET", BLACK,6, BLUE, action= reset)
b9 = Button(1050, 300, 120, 50, "Dfs", BLACK, 4, BLUE, action=dfs1)

text_1 = Button(950, 10, 300, 50, "Maze Generation Algorithms", BLACK,1, WHITE)
text_2 = Button(950, 200, 300, 50, "Maze Solving Algorithms", BLACK,1, WHITE)
text_3 = Button(950, 390, 300, 50, "Controls", BLACK, 1, WHITE)

def draw_nodes():
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    text_1.draw()
    text_2.draw()
    text_3.draw()

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
                    elif b5.rect.collidepoint(event.pos):
                        b5.action()
                    elif b6.rect.collidepoint(event.pos):
                        b6.action()
                    elif b7.rect.collidepoint(event.pos):
                        b7.action() 
                    elif b8.rect.collidepoint(event.pos):
                        b8.action() 
                    elif b9.rect.collidepoint(event.pos):
                        b9.action() 
                           
        screen.blit(control_surface, control_rect)
        screen.blit(maze_surface, maze_rect)
        draw_maze(grid)
        draw_nodes()
        
        pygame.display.update()
        clock.tick(60)
