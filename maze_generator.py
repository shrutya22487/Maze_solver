import random
import pygame
import time
from sys import exit
# import binary_tree

pygame.init()
width, height = 20, 20
FPS = 60
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
PINK = (210, 0, 210)
GRAY = (60, 60, 60)

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
        
        def check_dead_end(self):
            return (self.N + self.W +self.S +self.E ) == 1
        
        def fill_cell(self , x, y):
            if self.N == 1:
                self.N = 0
                if check_bounds(x - 1, y):
                    grid[y][x - 1].S = 0
            elif self.E == 1:
                self.E = 0
                if check_bounds(x , y + 1):
                    grid[y+1][x].W = 0
            elif self.W == 1:
                self.W = 0
                if check_bounds(x, y - 1):
                    grid[y - 1][x].E = 0
            elif self.S == 1:
                self.S = 0
                if check_bounds(x + 1, y):
                    grid[y][x + 1].N = 0                   

grid = [[Cell() for i in range(width)] for i in range(height)]

def fps60():
    global FPS
    FPS = 60
def fps5():
    global FPS
    FPS = 5
def fps1():
    global FPS
    FPS = 1
def fps40():
    global FPS
    FPS = 40    


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
            # if cell.S == 0:
            #     pygame.draw.rect(screen, BLUE, (cell_y, cell_x + CELL_SIZE, CELL_SIZE, wall_thickness))
            if cell.W == 0:
                pygame.draw.rect(screen, BLUE, (cell_y, cell_x, wall_thickness, CELL_SIZE))
            # if cell.E == 0:
            #     pygame.draw.rect(screen, BLUE, (cell_y + CELL_SIZE, cell_x, wall_thickness, CELL_SIZE))

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
        clock.tick(FPS)

def left_wall_follower():
    
    def rotate_clockwise():
        global directions
        keys = list(directions.keys())
        values = list(directions.values())
        values_right = [values[-1]]
        values_left = values[:-1]
        values_rotated = values_right + values_left
        directions = dict(zip(keys,values_rotated))

    def rotate_anti_clockwise():
        global directions
        keys = list(directions.keys())
        values = list(directions.values())
        values_right= values[1:]
        values_left = [values[0]]
        values_rotated = values_right + values_left
        directions = dict(zip(keys,values_rotated))

    def step_forward(x, y):
        global directions
        match directions['forward']:
            case 'E':
                return x, y + 1
            case 'W':
                return x,y-1
            case 'N':
                return x - 1, y
            case 'S':
                return x + 1 , y

    def draw_path(x, y):
        cell_x = x * CELL_SIZE
        cell_y = y * CELL_SIZE

        #figuring out where left wall is
        if directions['left'] == "N":
            pygame.draw.rect(screen, GREEN , (cell_y, cell_x,CELL_SIZE,wall_thickness))
        if directions['left'] == "S":
            pygame.draw.rect(screen, GREEN , (cell_y, cell_x + CELL_SIZE,CELL_SIZE,wall_thickness))
        if directions['left'] == "E":
            pygame.draw.rect(screen, GREEN , (cell_y + CELL_SIZE, cell_x,wall_thickness,CELL_SIZE))
        if directions['left'] == "W":
            pygame.draw.rect(screen, GREEN , (cell_y , cell_x ,wall_thickness,CELL_SIZE))

    x, y = width - 1, height - 1
    while not( x == 0 and y == 0 ) :
        #checking left wall
        if directions['left']=='E':
            if grid[y][x].E == 0:
                #checking front wall
                if directions['forward']=='E':
                    if grid[y][x].E == 0:
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)
                elif directions['forward']=='W':
                    if grid[y][x].W == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)
                    
                elif directions['forward']=='N':
                    if grid[y][x].N == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)    
                elif directions['forward']=='S':
                    if grid[y][x].S == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)  
            else:
                rotate_anti_clockwise()
                x, y = step_forward(x, y)               
        
        elif directions['left']=='N':
            if grid[y][x].N == 0:
                #checking front wall
                if directions['forward']=='E':
                    if grid[y][x].E == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)
                elif directions['forward']=='W':
                    if grid[y][x].W == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)
                    
                elif directions['forward']=='N':
                    if grid[y][x].N == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)    
                elif directions['forward']=='S':
                    if grid[y][x].S == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)  
            else:
                rotate_anti_clockwise()
                x, y = step_forward(x, y)  
            
        elif directions['left']=='W':
            if grid[y][x].W == 0:
                #checking front wall
                if directions['forward']=='E':
                    if grid[y][x].E == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)
                elif directions['forward']=='W':
                    if grid[y][x].W == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)
                    
                elif directions['forward']=='N':
                    if grid[y][x].N == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)    
                elif directions['forward']=='S':
                    if grid[y][x].S == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)  
            else:
                rotate_anti_clockwise()
                x, y = step_forward(x, y)  

        elif directions['left']=='S':
            if grid[y][x].S == 0:
                #checking front wall
                if directions['forward']=='E':
                    if grid[y][x].E == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)
                elif directions['forward']=='W':
                    if grid[y][x].W == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)
                    
                elif directions['forward']=='N':
                    if grid[y][x].N == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)    
                elif directions['forward']=='S':
                    if grid[y][x].S == 0:
                        
                        rotate_clockwise()
                    else:
                        x, y = step_forward(x, y)  
            else:
                rotate_anti_clockwise()
                x, y = step_forward(x, y)  
        draw_maze(grid)
        pygame.draw.rect(screen, PINK, (y* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, x* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
        draw_path(x, y)
        draw_nodes()
        pygame.display.update()    
        clock.tick(FPS)

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
        clock.tick(FPS)

def dikshtra():

    def draw_path(path):
        for i in path:
            pygame.draw.rect(screen, GREEN, (i[1]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, i[0]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
            pygame.time.delay(100)
            pygame.display.update()

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
    
    unvisited,reverse_path, visited = {}, {} , []
    #setting all the values in unvisited to infinity
    set_all_to_infinity()
    currcell = (width - 1, height - 1 )
    unvisited[currcell] = 0

    while unvisited:
        pygame.draw.rect(screen, PINK, ( currcell[1] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                    currcell[0] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                    SMALL_BLOCK_SIZE))
        currcell = min_cell()
        pygame.draw.rect(screen, RED ,( currcell[1] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                    currcell[0] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                    SMALL_BLOCK_SIZE))
        # pygame.draw.rect(screen, PINK, (currcell[1]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, currcell[0]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
        pygame.display.update()

        if currcell == (0, 0):
            break
        #make random here
        for i in "NEWS":

            childCell = 0
            if i == "E" and grid[currcell[1]][currcell[0]].E == 1:
                childCell = (currcell[0],currcell[1] + 1)

            elif i == "W" and grid[currcell[1]][currcell[0]].W == 1:
                childCell=(currcell[0],currcell[1] - 1)

            elif i == "S" and grid[currcell[1]][currcell[0]].S == 1:
                childCell=(currcell[0]+ 1 ,currcell[1])

            elif i == "N" and grid[currcell[1]][currcell[0]].N == 1:
                childCell=(currcell[0] - 1,currcell[1] )

            if childCell != 0 and childCell in visited:
                continue

            if childCell != 0 :
                pygame.draw.rect(screen, GRAY , ( childCell[1] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                    childCell[0] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                    SMALL_BLOCK_SIZE))
            
            temp_dist = unvisited[currcell] + 1
            
            pygame.display.update()

            if childCell != 0 and temp_dist < unvisited[childCell]:
                unvisited[childCell] = temp_dist
                reverse_path[childCell] = currcell
        
        pygame.display.update()
        visited.append(currcell)
        unvisited.pop(currcell)
        clock.tick(FPS)

    final_path = {}
    cell = (0,0)
    while cell != ( width - 1, height - 1):
        final_path[cell] = reverse_path[cell]
        cell = reverse_path[cell]
    reverse_list = list(final_path.values())
    forward_list = reverse_list[::-1]
    draw_path( forward_list ) 
    # print(reverse_path)
    pygame.time.delay(3000)

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
        pygame.draw.rect(screen, PINK, ( y * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                    x * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                    SMALL_BLOCK_SIZE))
        if (x, y) == (width - 1, height - 1):  # Reached the exit
            print("DFS Path Found!")
            pygame.time.delay(5000)
            return

        temp = get_unvisited_neighbors(x, y)
        if len(temp)==0:
            stack.remove((x,y))
            pygame.draw.rect(screen, GRAY, ( y * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                    x * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                    SMALL_BLOCK_SIZE))

        else:
            stack.extend(temp)

        draw_nodes()

        pygame.display.update()
        clock.tick(FPS)

    print("DFS: No Path Found!")

def dead_end_filler():
    def step(x, y):
        if grid[y][x].N == 1 and (x - 1, y) not in visited:
            return (x - 1, y)
        if grid[y][x].S == 1 and (x + 1, y) not in visited:
            return (x + 1, y)
        if grid[y][x].E == 1 and (x , y + 1) not in visited:
            return (x , y + 1)
        if grid[y][x].W == 1 and (x , y - 1) not in visited:
            return (x , y - 1)
        
    remaining_cells = True
    while remaining_cells:

        remaining_cells = False
        for x in range(width):
            for y in range(height):
                if grid[y][x].check_dead_end():
                    if (x, y) != (0, 0) and (x, y) != (width - 1, height - 1):
                        pygame.draw.rect(screen, PINK, (y* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, x* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
                        pygame.display.update()
                        grid[y][x].fill_cell(x, y)
                        remaining_cells = True
                clock.tick(FPS)          
            draw_maze(grid)
            pygame.display.update()
                
        

    currcell = (0, 0)
    visited = []
    while currcell != (width - 1, height - 1):
        pygame.draw.rect(screen, GREEN, (currcell[1]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, currcell[0]* CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
        pygame.display.update()
        visited.append(currcell)
        currcell = step(currcell[0], currcell[1])
        clock.tick(FPS)
    pygame.time.delay(3000)

def draw_solution_path(cell, visited):
    for x, y in visited:
        pygame.draw.rect(screen, PINK, (y * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                        x * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                        SMALL_BLOCK_SIZE))
    pygame.draw.rect(screen, PINK, (cell[1] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2,
                                    cell[0] * CELL_SIZE + (CELL_SIZE - SMALL_BLOCK_SIZE) // 2, SMALL_BLOCK_SIZE,
                                    SMALL_BLOCK_SIZE))

b1 = Button(800 ,70 , 120, 50, "Binary Tree", BLACK, 4,BLUE,  action = binary_tree)
b2 = Button(1300 ,70 , 120, 50, "Prims algo", BLACK,4, BLUE, action = prims_algorithm)
b3 = Button(800 ,250 , 180, 50, "Left wall follower", BLACK,4, BLUE, action = left_wall_follower)
b4 = Button(1300 ,250 , 120, 50, "Dikshtra", BLACK,4, BLUE, action= dikshtra)
b10 = Button(1030 ,340 , 150, 50, "Dead end filler", BLACK,4, BLUE, action= dead_end_filler)

b5 = Button(800, 470, 120, 50, "5 X 5" ,BLACK, 4, BLUE, action = fiveXfive)
b6 = Button(1050, 470, 120, 50, "10 X 10" ,BLACK, 4, BLUE, action = tenXten)
b7 = Button(1300, 470, 120, 50, "20 X 20" ,BLACK, 4, BLUE, action = twentyXtwenty)
b8 = Button(1050, 690, 120, 50, "RESET", BLACK,6, BLUE, action = reset)
b9 = Button(1050, 250, 120, 50, "Dfs", BLACK, 4, BLUE, action = dfs1)

b11 = Button(800, 580, 50, 50, "60", BLACK, 4, BLUE, action = fps60)
b12 = Button(1000, 580, 50, 50, "40", BLACK, 4, BLUE, action = fps40)
b13 = Button(1200, 580, 50, 50, "5", BLACK, 4, BLUE, action = fps5)
b14 = Button(1400, 580, 50, 50, "1", BLACK, 4, BLUE, action = fps1)

text_1 = Button(950, 10, 300, 50, "Maze Generation Algorithms", BLACK,1, WHITE)
text_2 = Button(950, 170, 300, 50, "Maze Solving Algorithms", BLACK,1, WHITE)
text_3 = Button(950, 420, 300, 50, "Size", BLACK, 1, WHITE)
text_4 = Button(950, 530, 300, 50, "FPS", BLACK, 1, WHITE)

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
    b10.draw()
    b11.draw()
    b12.draw()
    b13.draw()
    b14.draw()

    text_1.draw()
    text_2.draw()
    text_3.draw()
    text_4.draw()

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
                    elif b10.rect.collidepoint(event.pos):
                        b10.action() 
                    elif b11.rect.collidepoint(event.pos):
                        b11.action() 
                    elif b12.rect.collidepoint(event.pos):
                        b12.action()
                    elif b13.rect.collidepoint(event.pos):
                        b13.action() 
                    elif b14.rect.collidepoint(event.pos):
                        b14.action()                     
                           
        screen.blit(control_surface, control_rect)
        screen.blit(maze_surface, maze_rect)
        draw_maze(grid)
        draw_nodes()
        
        pygame.display.update()
        clock.tick(FPS)
