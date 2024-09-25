"""
WRITE YOUR PROGRAM HEADER HERE
"""
from SearchStructures import Stack, Queue
from Maze import Maze

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
         if (row > self.maze.num_rows and row < 0) and (col > self.maze.num_cols and col < 0):
             return False
         # Check if tile is a wall
         if self.maze.contents[row][col].isWall == True:
            return False
         # Check if tile has already been visited
         if self.maze.contents[row][col].visited == True:
            return False
         return True

    def solve(self):
        # ~~~~~~~~
        # Write your solve() implementation here
        # ~~~~~~~~
        # Add starting tile
        self.ss.add(maze.start)
        # As long as ss isn't empty
        while not self.ss.isEmpty():
            # Remove the next tile from ss and store it in current value
            current = self.maze.contents.remove()
            # Mark current as visited
            current.maze.visit
            # If current is the goal tile
            if current.goal == True:
                return current
            else:
                # Tile Movement (up, down, left, right) for current
                movement = ([-1][0],[0][+1],[1][0],[0][-1])
                for self.maze.contents in range(self.maze.contents[movement]):
                    # Set neighbor's previous tile to current
                    self.ss.__previous = current
                    # add neighbor to ss
                    self.ss.add(maze.__previous)
        return None
        pass

     # Add any other helper functions you might want here

    def getPath(self):
        # ~~~~~~~~
        # Write your getPath() implementation here
        # ~~~~~~~~
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