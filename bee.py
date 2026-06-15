from beehive import Beehive
from entity import Entity
import pygame

class Bee(Entity):

    bee_size = 5
    NECTAR_LIMIT = 10


    def __init__(self, id, screen):
        self._id = id
        self._x = 0
        self._y = 0
        self._speed = 1
        self._beehive = Beehive()
        self._nectar_count = 0
        
        self._screen = screen
        self._img = pygame.image.load("assets/bee_image.png").convert_alpha()
        self._rect = self._img.get_rect()
        self._rect.topleft = (0, 0)

    def move(self):
        pass
