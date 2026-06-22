import sys
import pygame
from config import *

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


    def run(self):
        # game state
        running = True

        # main game loop
        while running:
            # event handling loop
            for event in pygame.event.get():
                # check if user clicked close button
                if event.type == pygame.QUIT:
                    running = False

                # example keyboard input detection
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # move players, check collisions, update scores here

            # clear screen with a background color
            self.screen.fill(GRASS_GREEN)

            # draw game sprites and shapes here
            beehive = Beehive(50, 50, 50)
            for i in range(50):
                beehive.create_bee()
            for bee in beehive.bees:
                bee.draw()
            
            pygame.display.flip()

            self.clock.tick(FPS)


        pygame.quit()
        sys.exit()
