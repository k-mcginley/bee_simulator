from beehive import Beehive
from entity import Entity
from config import *
import pygame

class Bee(Entity):

    bee_size = 5
    bee_img = "assets/bee_image.png"


    def __init__(self, x, y, id, beehive: Beehive):
        super().__init__(x, y, Bee.bee_img)
        self._speed = 1
        self.beehive = beehive
        self._nectar_count = 0
        self._id = id
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.rect.topleft = (100, 100)

    def move(self):
        if beehive.x > self.x:
            self.x += self._speed
        elif beehive.x < self.x:
            self.x -= self._speed
        elif beehive.y > self.y:
            self.y += self._speed
        elif beehive.y < self.y:
            self.y -= self._speed

        
