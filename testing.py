import time
import random

width, height = 32,32
directions = {'forward':'N','left':'W','back':'S','right':'E'} #standard directions
number_of_turns = 0
total_steps = 0
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

def reset():
    global grid
    grid = [[Cell() for i in range(width)] for i in range(height)]

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

def left_wall_follower():
    
    def rotate_clockwise():
        global directions
        global number_of_turns
        number_of_turns += 1
        keys = list(directions.keys())
        values = list(directions.values())
        values_right = [values[-1]]
        values_left = values[:-1]
        values_rotated = values_right + values_left
        directions = dict(zip(keys,values_rotated))

    def rotate_anti_clockwise():
        global directions
        global number_of_turns
        number_of_turns += 1
        keys = list(directions.keys())
        values = list(directions.values())
        values_right= values[1:]
        values_left = [values[0]]
        values_rotated = values_right + values_left
        directions = dict(zip(keys,values_rotated))

    def step_forward(x, y):
        global directions
        global total_steps
        total_steps += 1
        match directions['forward']:
            case 'E':
                return x, y + 1
            case 'W':
                return x,y-1
            case 'N':
                return x - 1, y
            case 'S':
                return x + 1 , y

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

total_time = 0

def dikshtra():

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
        currcell = min_cell()

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

            
            temp_dist = unvisited[currcell] + 1
            

            if childCell != 0 and temp_dist < unvisited[childCell]:
                unvisited[childCell] = temp_dist
                reverse_path[childCell] = currcell
       

        visited.append(currcell)
        unvisited.pop(currcell)

    final_path = {}
    cell = (0,0)
    while cell != ( width - 1, height - 1):
        final_path[cell] = reverse_path[cell]
        cell = reverse_path[cell]
    reverse_list = list(final_path.values())
    global total_steps
    total_steps += len(reverse_list)

def dead_end_filler():
    def step(x, y):
        global total_steps 
        total_steps += 1
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
                        grid[y][x].fill_cell(x, y)
                        remaining_cells = True

    currcell = (0, 0)
    visited = []
    while currcell != (width - 1, height - 1):
        visited.append(currcell)
        currcell = step(currcell[0], currcell[1])

total_steps_list = []

for i in range(10):
    binary_tree()
    start_time = time.perf_counter()
    dead_end_filler()
    end_time = time.perf_counter()
    total_steps_list.append(total_steps*100/32/32)
    print(total_steps)
    total_steps = 0
    total_time = total_time + end_time - start_time
    reset()

# print("avg time taken  ", total_time * 10)
mean_perecentage = 0
for i in range(10):
    mean_perecentage += total_steps_list[i]
print("mean percentage", mean_perecentage/10)
print("percentage list: ", total_steps_list)