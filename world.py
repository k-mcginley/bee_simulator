import sys
import pygame
import random
from config import *

from beehive import Beehive
from bee import Bee
from flower import Flower

class World:

    def __init__(self):
        pygame.init()

        self.__temp = 5 #input("Input the world's temperature: ")
        self.__humidity = 5 #input("Input the world's humidity level: ")
        self.__air_pollution = 5 #int(input("Input the world's air pollution: "))
        self.__num_beehives = 2 #int(input("Input the starting number of beehives: "))
        self.__num_flowers = 20 #int(input("Input the number of flowers: "))
        self.__entities = []

        # pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Bee Simulator")
        self.clock = pygame.time.Clock()

        # make things - flowers, beehives
        for i in range(self.__num_beehives):
            hive_x = random.randint(100, SCREEN_WIDTH - 100)
            hive_y = random.randint(100, SCREEN_HEIGHT - 100)
            beehive = Beehive(hive_x, hive_y, self.__entities)

        for i in range(self.__num_flowers):
            flower_x = random.randint(100, SCREEN_WIDTH - 100)
            flower_y = random.randint(100, SCREEN_HEIGHT - 100)
            flower = Flower(flower_x, flower_y, self.__entities)
        
        
        


    def run(self):
        
        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # move players, check collisions, update scores 
            for entity in self.__entities:
                entity.update()

            # clear screen
            self.screen.fill(GRASS_GREEN)

            # draw game sprites and shapes 
            for entity in self.__entities:
                entity.draw(self.screen)

            for entity in self.__entities:
                if isinstance(entity, Beehive):
                    entity.draw(self.screen)

            for entity in self.__entities:
                if isinstance(entity, Flower):
                    entity.draw(self.screen)

            for entity in self.__entities:
                if isinstance(entity, Bee):
                    if not entity.inside_hive:
                        entity.draw(self.screen)
        

            pygame.display.flip()
            self.clock.tick(FPS)


        pygame.quit()
        sys.exit()
