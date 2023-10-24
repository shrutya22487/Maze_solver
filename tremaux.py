def is_valid_move(matrix, x, y):    #if the move made is within bounds
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != 0

def is_junction(matrix, x, y):
    valid_moves = sum(1 for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if is_valid_move(matrix, x + dx, y + dy))
    return valid_moves >= 3

def mark_entrance(matrix, x, y):        #marks entrance of a path based on it's previous marking value
    if matrix[x][y] == 1:
        matrix[x][y] = 2
        return True
    elif matrix[x][y] == 2:
        matrix[x][y] = 3
        return True
    
    return False

def dead_end(valid_moves):
    if len(valid_moves) == 1:
        return True
    return False

def tremaux(matrix):
    stack = []
    x,y, prev_x, prev_y  = 1, 1, 0, 0

    mark_entrance(matrix , x, y)                    # mark entrance path

    length = len(matrix)

    stack.append((x, y))

    while len(stack) > 0:

        x, y = stack.pop()

        if x == length - 2 and y == length - 2:         #Maze solved
            break

        valid_moves = [(dx, dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if is_valid_move(matrix, x + dx, y + dy)]# all possible movements available regardless of marking

        if is_junction(matrix, x, y):
            flag = False #to check if we found a way
            mark_entrance(matrix ,prev_x , prev_y) # mark the entrance u r leaving
            
            for i in valid_moves: #checking unmarked entrances

                possible_x, possible_y = i
                if matrix[possible_x][possible_y] == 1:
                    next_x, next_y = possible_x, possible_y 
                    mark_entrance(matrix, next_x , next_y)       
                    prev_x, prev_y = x, y
                    flag = True
                    break

            if (not flag and matrix[prev_x][prev_y] != 3): #go back the current path if not marked twice
                next_x, next_y = prev_x, prev_y
                mark_entrance(matrix, prev_x , prev_y)

            if ( not flag ):    #else pick any entrance marked once
                for i in valid_moves:  
                    if matrix[possible_x][possible_y] == 2:
                        next_x, next_y = possible_x, possible_y  
                        mark_entrance(matrix, next_x , next_y)      
                        prev_x, prev_y = x, y
                        break

        else:                   # otherwise it's a normal path continue as needed
            if dead_end(valid_moves):
                mark_entrance(matrix, x, y)
                next_x, next_y = x, y
            elif ( len(valid_moves) >= 2 ):
                valid_moves.remove((prev_x, prev_y))
            prev_x, prev_y = x, y
            next_x, next_y = valid_moves[0][0], valid_moves[0][1]

        stack.append((next_x ,next_y))




