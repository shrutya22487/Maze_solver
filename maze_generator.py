import numpy as np
import random

# Define the dimensions of the maze
maze_size = (20, 20)

# Create a maze filled with walls (0s) except for entry and exit points
maze = np.zeros(maze_size, dtype=int)
maze[0, :] = 1
maze[-1, :] = 1
maze[:, 0] = 1
maze[:, -1] = 1

# Define the entry and exit points
entry_point = (0, 1)
exit_point = (maze_size[0] - 1, maze_size[1] - 2)

# Set the entry and exit points
maze[entry_point] = 2
maze[exit_point] = 3

# Recursive Backtracking Algorithm
def recursive_backtracking(maze, current):
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(directions)
    
    for dx, dy in directions:
        new_x, new_y = current[0] + dx, current[1] + dy
        if 0 < new_x < maze_size[0] and 0 < new_y < maze_size[1]:
            if maze[new_x, new_y] == 0:
                maze[new_x, new_y] = 1
                maze[current[0] + dx // 2, current[1] + dy // 2] = 1
                recursive_backtracking(maze, (new_x, new_y))

# Start the recursive backtracking from the entry point
recursive_backtracking(maze, entry_point)

# Print the maze
for row in maze:
    print(' '.join(map(str, row)))

# Save the maze as a text file
np.savetxt('maze.txt', maze, fmt='%d')
