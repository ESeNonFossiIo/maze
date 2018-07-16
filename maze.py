from maze.maze import Maze

# Define the dimensions of the maze:
n, m = 15, 15

maze = Maze(n, m)

# Define the percentage of walls (respet to the whole number of elements) to add:
maze.make_maze(25)

# Define the starting and ending point:
maze.set_start(((2*n + 1)*(2*m + 1))-2-(2*m + 1))
maze.set_end(((2*n + 1)*(2*m + 1))//2+1)

# Show the maze before the solution:
maze.plot()

# Solve the maze:
maze.solve()

# Show the solution if there are any:
maze.plot()
