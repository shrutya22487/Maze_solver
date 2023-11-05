

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

    pygame.display.update()


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
    pygame.display.update()    
    pygame.time.delay(500)
