"""
Author: Kevin Avina-Gutierrez

Description: This file represents the current state of the game. Hold snake movement methods and 
CellNeighbor methods for cell implementation changes. 

Last updated on: 12/08/2024
"""

from boardCell import BoardCell
from preferences import Preferences

import random
from enum import Enum, auto


class GameData:
    def __init__(self):
        # Dimensions of the board (in cells)
        self.__height = Preferences.NUM_CELLS_TALL
        self.__width = Preferences.NUM_CELLS_WIDE

        # Keep track of how many cells are empty and in the board
        self.__freeCells = self.__height * self.__width
        self.__totalCells = self.__height * self.__width

        # The current movement mode of the snake (i.e., the current
        # direction or in AI mode
        self.__currentMode = self.SnakeMode.GOING_EAST

        #A 2D array of cells in the board
        self.__board = self.createBoard()

        # A list of cells that currently contain food (from oldest to newest)
        self.__foodCells = [] 
        # A list of cells that contain the snake (from head to tail)
        self.__snakeCells = []

        # Whether or not the game is over
        self.__gameOver = False

        # Initialize the score
        self.__score = 0

        # Number of food iteams eaten consecutively
        self.__consecutiveFood = 0

        # Speed multiplier for faster gameplay
        self.__speedMultiplier = 1.0

    ##########################
    # Initialization methods #
    ##########################

    def createBoard(self):
        """ Populate the starting state of the board.
            Returns a 2D array of cells in the board. """
        
        # Fill in the board with empty cells
        board = [[BoardCell(row, col) for col in range(self.__width)] 
                                        for row in range(self.__height)]
        # Change the left and right edges to walls
        for row in range(self.__height):
            board[row][0].becomeWall()
            board[row][self.__width-1].becomeWall() 
            # Make sure these cells are not counted as "free"
            self.__freeCells -= 2
        # Change the top and bottom edges to walls
        for col in range(1, self.__width-1):
            board[0][col].becomeWall()
            board[self.__height-1][col].becomeWall()
            # Make sure these cells are not counted as "free"
            self.__freeCells -= 2

        return board
        
    def placeSnakeAtStartLocation(self):
        """ Place the snake in the upper left corner, facing east """

        head = self.getCell(1, 2)
        body = self.getCell(1, 1)
        
        # Mark these cells as the head and body
        head.becomeHead()
        body.becomeBody()

        # Add these cells to the snake cells list
        self.__snakeCells.append(head)
        self.__snakeCells.append(body)

        # Set the starting direction of the snake as east
        self.__currentMode = self.SnakeMode.GOING_EAST

        # Make sure these cells are not counted as "free"
        self.__freeCells -= 2

    ###############################
    # Information about the board #
    ###############################

    def inAIMode(self):
        """ Returns a boolean indicating whether or not we are in AI mode """
        return self.__currentMode == self.SnakeMode.AI_MODE

    def getCell(self, row, col):
        """ Returns the cell at the given row and column.
            Inputs: row - The row to get (between 0 and height-1)
                    col - The column to get (between 0 and width-1)
            Returns: The cell in that location """
        if (row >= 0 and row < self.__height) and (col >= 0 and col < self.__width):
            return self.__board[row][col]
        else:
            raise Exception("getCell tried to access cell outside of board: ({}, {})".format(row, col))
        
    ########################
    # Food related methods #
    ########################

    def noFood(self):
        """ Returns a boolean indicating whether 
            or not there is food on the board """
        return len(self.__foodCells) == 0
    
    def addFood(self):
        """ Adds food to an open spont on the board """

        # Find a value between 1 and self.__height-1 (inclusive)
        row = random.randrange(1, self.__height)
        # Find a value between 1 and self.__width-1 (inclusive)
        col = random.randrange(1, self.__width)
        # Get the cell at that location
        cell = self.getCell(row, col)

        # If it is empty, add food
        if cell.isEmpty():
            cell.becomeFood()
            self.__foodCells.append(cell)
            self.__freeCells -= 1

        # Otherwise, only add food if over 30% of our cells are free
        elif self.__freeCells / self.__totalCells > 0.3:
            self.addFood()

        # Otherwise, there is too much food on the board already
        else:
            print("Not adding more food")

    ##########################
    # Snake movement methods #
    ##########################

    def eatFood(self, foodCell):
        """ Update the stae of the baor dto reflect food has been eaten """
        # Change the current head to a body
        self.getSnakeHead().becomeBody()

        # Food cell becomes new head
        foodCell.becomeHead()
        self.__snakeCells.append(foodCell)

        self.__foodCells.remove(foodCell)

    def snakeMovement(self, nextCell):
        """ Move the snake to the next cell on the board """
        # Change current cell assigned to the snakes head as part of the body
        self.getSnakeHead().becomeBody()

        # Assign the nextCell to become the snake's head
        nextCell.becomeHead()

        # Add new head cell to snakeCells list
        self.__snakeCells.insert(0, nextCell)

        # Remove the tail fo the snake
        self.__snakeCells.pop().becomeEmpty()

    ###############################
    # Methods to access neighbors #
    ###############################

    def getNorthNeighbor(self, cell): 
        """ Returns the cell to the north of the given cell """
        # Update values to return for the cell in the north direction
        return self.getCell(cell.getRow() - 1, cell.getCol())

    def getSouthNeighbor(self, cell):
        """ Returns the cell to the south of the given cell """
        # Update values to return for the cell in the south direction
        return self.getCell(cell.getRow() + 1, cell.getCol())
    
    def getEastNeighbor(self, cell):
        """ Returns the cell to the east of the given cell """
        # Update values to return for the cell in the east direction
        return self.getCell(cell.getRow(), cell.getCol() + 1)
    
    def getWestNeighbor(self, cell):
        """ Returns the cell to the west of the given cell """
        # Update values to return for the cell in the west direction
        return self.getCell(cell.getRow(), cell.getCol() - 1)
    
    def getHeadNorthNeighbor(self):
        """ Returns the cell to the north of the snake's head """
        return self.getNorthNeighbor(self.getSnakeHead())
    
    def getHeadSouthNeighbor(self):
        """ Returns the cell to the south of the snake's head """
        return self.getSouthNeighbor(self.getSnakeHead())
    
    def getHeadEastNeighbor(self):
        """ Returns the cell to the east of the snake's head """
        return self.getEastNeighbor(self.getSnakeHead())
    
    def getHeadWestNeighbor(self):
        """ Returns the cell to the west of the snake's head """
        return self.getWestNeighbor(self.getSnakeHead())
    
    def getNextCellInDir(self):
        """ Returns the next cell in the snake's path based
            on its current direction (self.__currentMode) """
        # Acquire current cell information for comparison
        currentCell = None

        # Check for each required argument to determine which cell direction we should change
        match self.__currentMode:
            case self.SnakeMode.GOING_NORTH:
                currentCell = self.getNorthNeighbor(self.getSnakeHead())
            case self.SnakeMode.GOING_SOUTH:
                currentCell = self.getSouthNeighbor(self.getSnakeHead())
            case self.SnakeMode.GOING_EAST:
                currentCell = self.getEastNeighbor(self.getSnakeHead())
            case self.SnakeMode.GOING_WEST:
                currentCell = self.getWestNeighbor(self.getSnakeHead())

        return currentCell


    def getNeighbors(self, center):
        """ Returns a set of the neighbors around the given cell """
        return {self.getNorthNeighbor(center),
                self.getSouthNeighbor(center),
                self.getEastNeighbor(center),
                self.getWestNeighbor(center)}
    
    def getRandomNeighbor(self, center):
        """ Returns a random empty neighbor of the given cell """
        neighbors = self.getNeighbors(center)
        for cell in neighbors:
            if cell.isEmpty():
                return cell 
        # If none of them are empty, just return the first one
        return random.choice(neighbors)
    
    ###################################
    # Methods to set the snake's mode #
    ###################################
    
    def setDirectionNorth(self):
        """ Set the direction as north """
        self.__currentMode = self.SnakeMode.GOING_NORTH

    def setDirectionSouth(self):
        """ Set the direction as south """
        self.__currentMode = self.SnakeMode.GOING_SOUTH 

    def setDirectionEast(self):
        """ Set the direction as east """
        self.__currentMode = self.SnakeMode.GOING_EAST

    def setDirectionWest(self):
        """ Set the direction as west """
        self.__currentMode = self.SnakeMode.GOING_WEST

    def setAIMode(self):
        """ Switch to AI mode """
        self.__currentMode = self.SnakeMode.AI_MODE

    ###############################
    # Methods to access the snake #
    ###############################

    def getSnakeHead(self):
        """ Return the cell containing the snake's head """
        return self.__snakeCells[0]
    
    def getSnakeTail(self):
        """ Return the cell containing the snake's tail """
        return self.__snakeCells[-1]
    
    def getSnakeNeck(self):
        """ Return the body cell adjacent to the snake's head """
        return self.__snakeCells[1]

    #################################
    # Helper method for the display #
    #################################
    
    def getCellColor(self, row, col):
        """ Returns the color of the cell at the given location.
            Inputs: row - The row of the cell to access
                    col - The column of the cell to access """
        return self.getCell(row, col).getCellColor()
    
    ################################
    # Helper method(s) for reverse #
    ################################

    """ These methods help us implement the reverse movement method in our Controller.py file
        - unableHead
        - reverseSnakeCells
        - relableNewHead
        - updateSnakeDirection
    """
    def unlabelHead(self): 
        # Change the current head into a body cell by unlabeling the Head
        self.getSnakeHead().becomeBody()
    
    def reverseSnakeCells(self):
        # Reverse the list of cells that make up the snake
        self.__snakeCells = self.__snakeCells[::-1]
    
    def relabelNewHead(self):
        # Label the new head after reversing the snake
        self.getSnakeHead().becomeHead()
    
    def updateSnakeDirection(self):
        # Calculate and Updates the snake's direction based on 
        # the new head and neck position
        head = self.getSnakeHead()
        neck = self.getSnakeNeck()

        if head.getRow() < neck.getRow():
            self.setDirectionNorth()
        elif head.getRow() > neck.getRow():
            self.setDirectionSouth()
        elif head.getCol() < neck.getCol():
            self.setDirectionWest()
        elif head.getCol() > neck.getCol():
            self.setDirectionEast()

    #################################
    # Methods for AI implementation #
    #################################

    def resetCellsForSearch(self):
        for row in self.__board:
            for cell in row:
                cell.clearSearchInfo()
    
    #########################
    # Methods for Game over #
    #########################

    def setGameOver(self):
        """ Set the game over flag to True """
        self.__gameOver = True 

    def getGameOver(self):
        """ Check the game over value """
        return self.__gameOver
    
    ##############################
    # Methods for Tracking Score #
    ##############################

    def getScore(self):
        """ Return the current score """
        return self.__score
    
    def increaseScore(self, amount = 1):
        """ Increase the score by a given amount """
        self.__score += amount
        self.__consecutiveFood += 1

    #######################################
    # Methods for Speed Boost on a streak #
    #######################################

    def resetConsecutiveFood(self):
        """ Reset's the streak of consecutive food eaten """
        self.__consecutiveFood = 0

    def getConsecutiveFood(self):
        """ Return the number of consecutive food items eaten """
        return self.__consecutiveFood
    
    def getSpeedMultiplier(self):
        """ Return the current speed multiplier """
        return self.__speedMultiplier
    
    ######################################
    # Helpers for printing and debugging #
    ######################################

    def __str__(self):
        """ Returns a string representation of the board """
        out = ""
        for row in self.__board:
            for cell in row:
                out += str(cell)
            out += "\n"
        return out
    
    def toStringParents(self):
        """ Returns a string representation of the parents of each cell """
        out = ""
        for row in self.__board:
            for cell in row:
                out += "{}\t".format(cell.parentString())
            out += "\n"
        return out

    class SnakeMode(Enum):
        """ An enumeration (or enum) to represent the valid
            SnakeModes, in order to ensure that we do not accidentally
            use an invalid mode. The auto() is used when the value of
            the objects does not matter.
        """
        GOING_NORTH = auto()
        GOING_SOUTH = auto()
        GOING_EAST = auto()
        GOING_WEST = auto()
        AI_MODE = auto()