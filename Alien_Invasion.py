import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manager game assets and behavior"""

    def __innit__(self):
        "Initialize the game, and create game resouces"
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        #Set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the gamee"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            #Make the most recently drawn screen invisible.
            pygame.display.flip()


if __name__ == '_main_':
#make a game instance , and run this game.
    ai = AlienInvasion()
    ai.run_game()

