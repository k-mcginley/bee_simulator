import sys
import pygame

from world import World
from beehive import Beehive
from flower import Flower


pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
FPS = 60

# Color definitions (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    world = World()

