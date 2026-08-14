from beehive import Beehive
from entity import Entity
from config import *
import pygame

class Bee(Entity):

    bee_size = 5
    bee_img = "assets/bee_right.png"


    def __init__(self, x, y, id, beehive: Beehive):
        super().__init__(x, y, Bee.bee_img)
        self.speed = 1
        self.beehive = beehive
        self.nectar_count = 0
        self.id = id

    def move_towards(self, target_pos):
        target = pygame.math.Vector2(target_pos)
        current = pygame.math.Vector2(self.rect.center)

        distance = current.distance_to(target)

        if distance > 0:
            if distance < self.speed:
                self.rect.center = target_pos
            else:
                direction = (target - current).normalize()
                new_pos = current + direction * self.speed
                self.rect.center = (int(new_pos.x), int(new_pos.y))

        '''
        if target.x > self.x:
            self.x += self._speed
        elif target.x < self.x:
            self.x -= self._speed
        elif target.y > self.y:
            self.y += self._speed
        elif target.y < self.y:
            self.y -= self._speed
        '''
        
    def update(self):
        hive_target = (self.beehive.x, self.beehive.y)
        self.move_towards(hive_target)