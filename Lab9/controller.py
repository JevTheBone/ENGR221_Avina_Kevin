"""
Author: Kevin Avina-Gutierrez

Description: The Controller of the game, including handling key presses
(and AI in the next assignment). You will update this file.

Last updated on: 12/08/2024
"""

from preferences import Preferences
from gameData import GameData
from boardDisplay import BoardDisplay

import pygame
from enum import Enum
from queue import Queue

class Controller():
    def __init__(self):
        # The current state of the board
        self.__data = GameData()
        # The display
        self.__display = BoardDisplay()
        # How many frames have passed
        self.__numCycles = 0

        # Attempt to load any sounds and images
        try:
            pygame.mixer.init()
            self.__audioEat = pygame.mixer.Sound(Preferences.EAT_SOUND)
            self.__display.headImage = pygame.image.load(Preferences.HEAD_IMAGE)
        except:
            print("Problem error loading audio / images")
            self.__audioEat = None

        # Initialize the board for a new game
        self.startNewGame()
        
    def startNewGame(self):
        """ Initializes the board for a new game """

        # Place the snake on the board
        self.__data.placeSnakeAtStartLocation()

    def gameOver(self):
        """ Indicate that the player has lost """
        self.__data.setGameOver()

    def run(self):
        """ The main loop of the game """

        # Keep track of the time that's passed in the game 
        clock = pygame.time.Clock()

        # Loop until the game ends
        while not self.__data.getGameOver():
            # Run the main behavior
            self.cycle() 
            # Adjust the sleep time dynamically
            baseSpeed = Preferences.SLEEP_TIME
            currentSpeed = baseSpeed / self.__data.getSpeedMultiplier()
            clock.tick(currentSpeed)

    def cycle(self):
        """ The main behavior of each time step """

        # Check for user input
        self.checkKeypress()
        # Update the snake state
        self.updateSnake()
        # Update the food state
        self.updateFood()
        # Increment the number of cycles
        self.__numCycles += 1
        # Update the display based on the new state
        self.__display.updateGraphics(self.__data)

    def checkKeypress(self):
        """ Update the game based on user input """
        # Check for keyboard input
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                self.gameOver()
            # Change the snake's direction based on the keypress
            elif event.type == pygame.KEYDOWN:
                # Reverse direction of snake
                if event.key in self.Keypress.REVERSE.value:
                    self.reverseSnake()
                # Enter AI mode
                elif event.key in self.Keypress.AI.value:
                    self.__data.setAIMode()

                # Changes direction to the right
                elif event.key in self.Keypress.RIGHT.value:
                    self.__data.setDirectionEast()

                # Changes direction going up
                elif event.key in self.Keypress.UP.value:
                    self.__data.setDirectionNorth()

                # Changes direction to the left
                elif event.key in self.Keypress.LEFT.value:
                    self.__data.setDirectionWest()

                # Changes direction going down
                elif event.key in self.Keypress.DOWN.value:
                    self.__data.setDirectionSouth()

    def updateSnake(self):
        """ Move the snake forward one step, either in the current 
            direction, or as directed by the AI """

        # Move the snake once every REFRESH_RATE cycles
        if self.__numCycles % Preferences.REFRESH_RATE == 0:
            # Find the next place the snake should move
            if self.__data.inAIMode():
                nextCell = self.getNextCellFromBFS()
            else:
                nextCell = self.__data.getNextCellInDir()
            try:
                # Move the snake to the next cell
                self.advanceSnake(nextCell)
            except:
                print("Failed to advance snake")

    def advanceSnake(self, nextCell):
        """ Update the state of the world to move the snake's head to the given cell """

        # If we run into a wall or the snake, it's game over
        if nextCell.isWall() or nextCell.isBody():
            self.gameOver()
        
        # If we eat food, update the state of the board
        elif nextCell.isFood():
            self.playSound_eat()

            self.__data.eatFood(nextCell)
            # Update the score
            self.__data.increaseScore()

            # Increase speed after every certain consecutive food items eaten
            if self.__data.getConsecutiveFood() % 2 == 0:
                self.__data.__speedMultiplier += 10
        else: 
            # Move snake to the next cell
            self.__data.snakeMovement(nextCell)
            # Reset streak if no food is eaten
            self.__data.resetConsecutiveFood()


    def updateFood(self):
        """ Add food every FOOD_ADD_RATE cycles or if there is no food """
        if self.__data.noFood() or (self.__numCycles % Preferences.FOOD_ADD_RATE == 0):
            self.__data.addFood()

    def getNextCellFromBFS(self):
        """ Uses BFS to search for the food closest to the head of the snake.
            Returns the *next* step the snake should take along the shortest path
            to the closest food cell. """
        
        # Parepare all the tiles to search
        self.__data.resetCellsForSearch()

        # Initialize a queue to hold the tiles to search
        cellsToSearch = Queue()

        # Add the head to the queue and mark it as added
        head = self.__data.getSnakeHead()
        head.setAddedToSearchList()
        cellsToSearch.put(head)

        # Search!
        while not cellsToSearch.empty():

            currentCell = cellsToSearch.get() # get the next cell in the queue

            # If we found food, return the first cell in the path to it
            if currentCell.isFood(): 
                return self.getFirstCellInPath(currentCell)
            
            # Otherwise, add all the neighbors to the queue
            for neighbor in self.__data.getNeighbors(currentCell):

                # If the neighbor is not already added to the search list and is not a wall, add it
                if not neighbor.alreadyAddedToSearchList() and not neighbor.isWall() and not neighbor.isBody():
                    neighbor.setAddedToSearchList()
                    neighbor.setParent(currentCell)
                    cellsToSearch.put(neighbor)

        # If the search failed, return a random neighbor
        return self.__data.getRandomNeighbor(head)

    def getFirstCellInPath(self, foodCell):
        """ Helper method that returns the first cell in the path to the food cell """

        currentCell = foodCell # start at the food cell

        # Keep moving back until we find the head of the snake
        while currentCell.getParent() != self.__data.getSnakeHead():
            currentCell = currentCell.getParent()

        #print("First cell in path: ", currentCell) # debugging
        return currentCell # return the cell that brings the snake to the food the fastest
    
    def reverseSnake(self):
        """ ReverseSnake method should change the current direction of the snake
            while updating the head/body's cell accordingly. """
    
        self.__data.unlabelHead() # Update the snake's head position relative to the body by unlabeling current head
    
        self.__data.reverseSnakeCells() # Reverse the snake's body based on the current body cells
    
        self.__data.relabelNewHead() # Relabel the new head according to its relative position in the opposite direction
    
        self.__data.updateSnakeDirection() # Recalculate direction of the snake based on the body/heads last position.

    def playSound_eat(self):
        """ Plays an eating sound """
        if self.__audioEat:
            pygame.mixer.Sound.play(self.__audioEat)
            pygame.mixer.music.stop()

    class Keypress(Enum):
        """ An enumeration (enum) defining the valid keyboard inputs 
            to ensure that we do not accidentally assign an invalid value.
        """
        UP = pygame.K_i, pygame.K_UP        # i and up arrow key
        DOWN = pygame.K_k, pygame.K_DOWN    # k and down arrow key
        LEFT = pygame.K_j, pygame.K_LEFT    # j and left arrow key
        RIGHT = pygame.K_l, pygame.K_RIGHT  # l and right arrow key
        REVERSE = pygame.K_r,               # r
        AI = pygame.K_a,                    # a


if __name__ == "__main__":
    Controller().run()