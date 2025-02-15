"""
Author: Kevin Avina-Gutierrez

Description: Creates and displays the graphics based on the current state of the board.
We can make changes allowing us to draw the argument gameData

Last updated on: 12/08/2024
"""

import pygame
from preferences import Preferences

class BoardDisplay:
    def __init__(self):
        # The display where the board is drawn
        self.__display = pygame.display.set_mode((Preferences.GAME_BOARD_WIDTH, Preferences.GAME_BOARD_HEIGHT))
        # Image to show as the "head"
        self.headImage = None
        # Rendering the score on the screen with a set font
        self.font = pygame.font.SysFont("arial", 36)

    def updateGraphics(self, gameData):
        """ Re-draws the board, food, and snake based
            on the current state of the board """
        
        # Clear the board
        self.clear()
        
        # Using row and columns coordinates to draw our cells
        # Iterate through each row in the board
        for row in range(Preferences.NUM_CELLS_TALL):
            # Iterate through each column in the board 
            for col in range(Preferences.NUM_CELLS_WIDE):
                # gameData gets the state of each cell to input into drawSquare to draw
                self.drawSquare(gameData.getCell(row, col)) 

        # Draw the game over message, if appropriate
        if gameData.getGameOver():
            self.displayGameOver()

        # Draw the score on the screen
        self.drawScore(self.__display, gameData.getScore())

        # Update the display
        pygame.display.update()

    def clear(self):
        """ Resets the background of the display """
        self.__display.fill(Preferences.COLOR_BACKGROUND)

    def drawSquare(self, cell):#row, col, cellColor):
        """ Draws a cell-sized square at the given location.
            Inputs: row - row coordinate of the square to draw
                    col - column coordinate of the square to draw
                    cellColor - color of the square to draw """
        row = cell.getRow()
        col = cell.getCol()

        if cell.isHead() and self.headImage:
            self.drawImage(row, col, self.headImage)
        else:
            cellColor = cell.getCellColor()
            pygame.draw.rect(self.__display, cellColor, [col*Preferences.CELL_SIZE, row*Preferences.CELL_SIZE, 
                                                     Preferences.CELL_SIZE, Preferences.CELL_SIZE])

    def drawImage(self, row, col, image):
        """ Displays an image at the given cell location.
            Inputs: row - row coordinate to draw the image at
                    col - column coordinate to draw the image at
                    image - the pygame image to draw """

        # First, convert the image to a Surface type (with transparent background)
        image = image.convert_alpha()
        # You will want to uncomment the below line if you want your image to fit within one cell
        #image = pygame.transform.scale(image, (Preferences.CELL_SIZE, Preferences.CELL_SIZE))
        # Grab the dimensions of the image
        imageRect = image.get_rect()
        # Place the image in the center of the given cell coordinates
        imageRect.center = ((col*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2),
                            (row*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2))
        # Place the image on the display
        self.__display.blit(image, imageRect)

    def displayGameOver(self):
        """ Displays the game over message """

        # Get the font
        font = Preferences.GAME_OVER_FONT
        # Create the text
        text = font.render(Preferences.GAME_OVER_TEXT, True, Preferences.GAME_OVER_COLOR)
        # Get the dimensions of the text box
        textRect = text.get_rect()
        # Specify the location of the text
        textRect.center = (Preferences.GAME_OVER_X, Preferences.GAME_OVER_Y)
        # Place the game over text on the display
        self.__display.blit(text, textRect)
    
    def drawScore(self, screen, score):
        """ Display the score on the screen """
        scoreText = self.font.render(f"Score: {score}", True, pygame.Color('black'))
        # Adjust the position of the score on the board
        screen.blit(scoreText, (25, 20))