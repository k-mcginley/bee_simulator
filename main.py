import sys
import pygame

from world import World


pygame.init()


def main():
    world = World()
    world.run()

