# Maze Solver 🧩

Welcome to the Maze Solver repository! This project demonstrates various maze generation and solving algorithms using the Pygame library. Dive into the fascinating world of algorithms and watch them come to life with real-time visualizations!

## 🎥 Demo

Check out our demo video on YouTube to see the Maze Solver in action: [Watch the demo](https://www.youtube.com/watch?v=JTPKxtpIqa0)

## 🖼️ Gallery
Here's a glimpse of the magic:

### Maze Generation

<img src="images\image-1.png" width="100%" alt="Maze Generation 1">

### Maze Solving
<div style="display: flex; flex-wrap: wrap; gap: 20px;">
  <img src="images\image-3.png" width="400" alt="Maze Generation 2">
  <img src="images\image.png" width="400" alt="Maze Generation 2">
</div>
  <img src="images\image-4.png" width="400" alt="Maze Generation 2">
  
## 🚀 Features

- **Maze Generation**: Create intricate mazes using:
  - Binary Tree Algorithm
  - Prim's Algorithm
- **Maze Solving**: Find your way through the maze with:
  - Left Wall Follower
  - Dijkstra's Algorithm
  - Depth-First Search (DFS)
  - Dead End Filler
- **Visualization**: Enjoy real-time visualization of both maze generation and solving processes.

## 📋 Requirements

- Python 3
- Pygame library

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shrutya22487/Maze_solver.git
   cd Maze_solver

2. Install dependencies
    ```bash
    pip install pygame

## 🎮 Controls

### Maze Generation Algorithms
- **Binary Tree**: `binary_tree()`
- **Prim's Algorithm**: `prims_algorithm()`

### Maze Solving Algorithms
- **Left Wall Follower**: `left_wall_follower()`
- **Dijkstra's Algorithm**: `dijkstra()`
- **Depth-First Search (DFS)**: `dfs()`

### Grid Size Controls
- **5x5 Grid**: `initialize_grid(5, 5)`
- **10x10 Grid**: `initialize_grid(10, 10)`
- **20x20 Grid**: `initialize_grid(20, 20)`

### Reset Grid
- **Reset**: `initialize_grid(width, height)`

## 📄 Documentation
# Maze Generation Algorithms

**Binary Tree Algorithm:** 🌲 This algorithm generates a maze by carving passages from each cell, connecting either to the north or east neighbor randomly, resulting in mazes with a strong diagonal bias.

**Prim's Algorithm:** 🌟 An algorithm that starts with a grid full of walls and adds walls to the maze by growing a spanning tree. It selects the next cell to carve based on the closest distance, creating more complex and varied mazes.

# Maze Solving Algorithms

**Left Wall Follower:** 🔄 A simple algorithm where you keep your left hand on the wall and move forward. Effective for solving mazes with loops and simple structures, but doesn't guarantee the shortest path.

**Dijkstra's Algorithm:** 🚀 A pathfinding algorithm that finds the shortest path from the start to the end of the maze by evaluating the cost of each neighboring node. It ensures the shortest possible path in weighted graphs.

**Depth-First Search (DFS):** 🌐 This algorithm explores as far as possible along each branch before backtracking, ensuring all paths are explored. Useful for finding a solution in mazes but doesn’t guarantee the shortest path.

**Dead End Filler:** ☠️ This algorithm solves the maze by identifying dead ends and filling them until only the correct path remains. Efficient in removing unnecessary paths but works best in mazes with many dead ends.

For detailed information on the algorithms and their implementations, refer to the project report and analysis files provided in the repository.
