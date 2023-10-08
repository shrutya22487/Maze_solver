import random
def tremaux(matrix):
    stack ,single_marked , double_marked , visited = [],[],[],[]
    x,y , w = 0 , 0, 1
    while len(stack) > 0:                                          # loop until stack is empty
        cell = []                                                  # define cell list
        if (x + w, y) not in visited and (x + w, y) in matrix:       # right cell available?
            cell.append("right")                                   # if yes add to cell list

        if (x - w, y) not in visited and (x - w, y) in matrix:       # left cell available?
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in matrix:     # down cell available?
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in matrix:      # up cell available?
            cell.append("up")

        if len(cell) > 0:                                          # check to see if cell list is empty
            cell_chosen = (random.choice(cell))                    # select one of the cell randomly

            if cell_chosen == "right":                             # if this cell has been chosen
                push_right(x, y)                                   # call push_right function
                solution[(x + w, y)] = x, y                        # solution = dictionary key = new cell, other = current cell
                x = x + w                                          # make this cell the current cell
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))                                # place current cell on to stack

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            single_cell(x, y)                                     # use single_cell function to show backtracking image
            time.sleep(.05)                                       # slow program down a bit
            backtracking_cell(x, y) 




