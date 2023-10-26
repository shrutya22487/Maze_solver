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

def tremaux(matrix):

    x,y, prev_x, prev_y  = 1, 1, 0, 0

    mark_entrance(matrix , x, y)                    # mark entrance path

    length = len(matrix)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        #adding surfaces
        screen.blit(background , (0,0)) 
        screen.blit(maze_surface , (50 , 50))

        pygame.display.update()
        clock.tick(10)

        if x == length - 2 and y == length - 2:         #Maze solved
            break

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
                prev_x, prev_y = x, y
                next_x, next_y = valid_moves[0][0], valid_moves[0][1]

            elif ( len(valid_moves) >= 2 ):
                valid_moves.remove((prev_x, prev_y))
                prev_x, prev_y = x, y
                next_x, next_y = valid_moves[0][0], valid_moves[0][1]
              
        x, y = next_x, next_y
        pygame.draw.rect(maze_surface , TEMP , ( 1 + 30 * x ,1 + 30 * y ,30 ,30 ) ,4)





