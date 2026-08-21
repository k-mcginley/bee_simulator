
from entity import Entity
from config import *
import pygame

class Bee(Entity):

    bee_size = 5
    bee_img = "assets/bee_right.png"


    def __init__(self, x, y, id, beehive):
        super().__init__(x, y, Bee.bee_img)
        self.speed = 1
        self.beehive = beehive
        self.nectar_count = 0
        self.id = id


    def move_towards(self, target_pos):
        target = pygame.math.Vector2(target_pos)
        self.pos = pygame.math.Vector2(self.rect.center)

        distance = self.pos.distance_to(target)

        if distance > 0:
            if distance <= self.speed:
                self.rect.center = target_pos
            else:
                direction = (target - self.pos).normalize()
                self.pos += direction * self.speed
                self.rect.center = (self.pos.x, self.pos.y)


        
    def update(self): # change so that targt can change
        hive_target = (self.beehive.x, self.beehive.y)
        self.move_towards(hive_target)