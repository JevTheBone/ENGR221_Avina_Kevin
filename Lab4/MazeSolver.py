"""
Name: Kevin Avina-Gutierrez
MazeSolver.py
Description: Implement an algorithm to find a path between two points in a 2D grid leveraging
your Stack and Queue classes from SearchStructures.py
"""
from .SearchStructures import Stack, Queue
from .Maze import Maze

class MazeSolver:
    # Constructor
    # Inputs:
    #   maze: The maze to solve (Maze)
    #   searchStructure: The search structure class to use (Stack or Queue)
    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object

    def tileIsVisitable(self, row:int, col:int) -> bool:
         # Check if the tile is within the maze bounds
         if (row >= self.maze.num_rows or row < 0) or (col >= self.maze.num_cols or col < 0):
             return False
         # Check if tile is a wall
         if (self.maze.contents[row][col].isWall() == True):
            return False
         # Check if tile has already been visited
         if (self.maze.contents[row][col].visited() == True):
            return False
         return True

    def solve(self):
        # Add starting tile
        self.ss.add(self.maze.start)
        # As long as ss isn't empty
        while not self.ss.isEmpty():
            # Remove the next tile from ss and store it in current value
            current = self.ss.remove()
            # Mark current as visited
            current.visit()
            # If current tile in the maze is the goal tile
            if current == self.maze.goal:
                self.ss.add(current)
                return current
            # Tile Movement (up, down, right, left) for current
            movement = [(0,-1),(0,1),(1,0),(-1,0)]
            # For i = row and j = col, adjust current row and col values by adding the directions of movement
            for i, j in reversed(movement):
                # If tile is visitable by adding i and j to the current values
                if self.tileIsVisitable(current.getRow() + i, current.getCol() + j):
                    # Then update the values by adding i and j to current tile and assign it to "next tile"
                    next_tile = self.maze.contents[current.getRow() + i][current.getCol() + j]
                    # Sets the previous tile prior to next.tile
                    next_tile.setPrevious(current)
                    # Add next tile to SearchStructures.py
                    self.ss.add(next_tile)
        return None

     # Add any other helper functions you might want here

    def getPath(self):
        # ~~~~~~~~
        # Write your getPath() implementation here
        # ~~~~~~~~
        path = []
        end = self.maze.goal
        last = end.getPrevious()
        # While the last visited tile isn't None or the start of the maze
        while last is not None and last != self.maze.start:
            # Add last tile to Path list
            path.append(last)
            # Sets our previous to the tile prior to last
            last = last.getPrevious()
        path.append(self.maze.start)
        return path[::-1]
        pass 

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##E",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()