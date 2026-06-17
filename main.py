import sys
import pygame

from world import World
from beehive import Beehive
from flower import Flower


pygame.init()


def main():
    world = World()
    world.run()

