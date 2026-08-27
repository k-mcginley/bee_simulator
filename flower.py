import random
from entity import Entity
from config import *

class Flower(Entity):

    num_flowers = 0
    flower_imgs = ["assets/flower_1.png", "assets/flower_2.png", "assets/flower_3.png", "assets/flower_4.png", "assets/flower_5.png"]
    flowers = []

    def __init__(self, x, y, entities):
        rand_num = random.randint(0, 4)
        super().__init__(x, y, entities, Flower.flower_imgs[rand_num])
        Flower.num_flowers += 1
        #Flower.flower_locations.append((self.x, self.y))
        self.id = Flower.num_flowers
        Flower.flowers.append(self)
        
        
        self.nectar_count = STARTING_NECTAR_COUNT
        self.nectar_timer = 0


    def update(self):
            """nectar creation timer"""
            if self.nectar_count < STARTING_NECTAR_COUNT:
                self.nectar_timer += 1
                if self.nectar_timer >= NECTAR_INTERVAL:
                    self.nectar_count += 1
                    self.nectar_timer = 0
