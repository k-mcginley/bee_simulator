import sys
import pygame
from config import *

from beehive import Beehive
from bee import Bee

class World:

    def __init__(self):
        pygame.init()

        self.__temp = 5 #input("Input the world's temperature: ")
        self.__humidity = 5 #input("Input the world's humidity level: ")
        self.__air_pollution = 5 #int(input("Input the world's air pollution: "))
        self.__num_beehives = 5 #int(input("Input the starting number of beehives: "))
        self.__num_flowers = 5 #int(input("Input the number of flowers: "))
        self.__entities = []

        # pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Bee Simulator")
        self.clock = pygame.time.Clock()


        self.beehive = Beehive(100, 100, 50)
        self.__entities.append(self.beehive)
        
        for i in range(50):
            bee = Bee(400, 400, i, self.beehive)
            self.__entities.append(bee)
        


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
            for entity in self.__entities:
                entity.update()

            # clear screen with a background color
            self.screen.fill(GRASS_GREEN)

            # draw game sprites and shapes here
            for entity in self.__entities:
                entity.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)


        pygame.quit()
        sys.exit()
