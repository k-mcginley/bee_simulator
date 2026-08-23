import random
from entity import Entity
from config import *

class Flower(Entity):

    num_flowers = 0
    flower_imgs = ["assets/flower_1.png", "assets/flower_2.png", "assets/flower_3.png", "assets/flower_4.png", "assets/flower_5.png"]

    def __init__(self, x, y, entities):
        rand_num = random.randint(0, 4)
        super().__init__(x, y, Flower.flower_imgs[rand_num])
        Flower.num_flowers += 1
        self.id = Flower.num_flowers
        
        self.nectar_count = STARTING_NECTAR_COUNT
        self.nectar_timer = 0
        self.nectar_interval = 180

        self.entity_list = entities
        self.entity_list.append(self) 

    def update(self):
            """nctar creation timer"""
            if self.nectar_count < STARTING_NECTAR_COUNT:
                self.nectar_timer += 1
                if self.nectar_timer >= self.nectar_interval:
                    self.nectar_count += 1  # use honey
                    self.nectar_timer = 0   # reset timer
