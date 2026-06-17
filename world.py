import sys
import pygame
from config import *
from beehive import Beehive

class World:
    def __init__(self):
        self.__temp = input("Input the world's temperature: ")
        self.__humidity = input("Input the world's humidity level: ")
        self.__air_pollution = int(input("Input the world's air pollution: "))
        self.__num_beehives = int(input("Input the starting number of beehives: "))
        self.__num_flowers = int(input("Input the number of flowers: "))
        self.__entities = []

        # pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Pygame Window")
        self.clock = pygame.time.Clock()

        # constraints:
        self.__MAX_BEES = 10000

    def run(self):
        # Game state variable
        running = True

        # 5. Main Game Loop
        while running:

            # --- Event Handling Loop ---
            for event in pygame.event.get():
                # Check if user clicked the window's close button
                if event.type == pygame.QUIT:
                    running = False

                # Example Keyboard input detection
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # --- Game Logic / State Updates ---
            # (Move players, check collisions, update scores here)

            # --- Drawing / Rendering Code ---
            # Clear screen with a background color
            self.screen.fill(GRASS_GREEN)

            # (Draw your game sprites and shapes here)
            beehive = Beehive(50, 50, 50)
            for i in range(50):
                beehive.create_bee()
            for bee in beehive.bees:
                bee.draw()
            

            # Refresh the screen display
            pygame.display.flip()

            # --- Frame Rate Management ---
            # Limits the loop to the specified FPS
            self.clock.tick(FPS)

        # 6. Clean Up and Exit
        pygame.quit()
        sys.exit()
