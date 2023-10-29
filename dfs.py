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