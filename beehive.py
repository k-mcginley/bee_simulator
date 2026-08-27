import random
from entity import Entity
from bee import Bee
from config import *

class Beehive(Entity):

    num_beehives = 0
    beehive_img = "assets/beehive_1.png"

    def __init__(self, x, y, entities):
        super().__init__(x, y, entities, Beehive.beehive_img)
        Beehive.num_beehives += 1
        self._id = Beehive.num_beehives

        self.larva_count = 5
        self.honey_count = STARTING_HONEY_COUNT
        self.bees = []

        self.spawn_timer = 0

        for i in range(20): # starts w 20 bees
            self.create_bee()


    def create_bee(self):
        if len(self.bees) < MAX_CAPACITY:
            spawn_x = self.rect.centerx + random.randint(-200, 200) # bee spawn outside - delete later
            spawn_y = self.rect.centery + random.randint(-200, 200)
            
            new_bee = Bee(spawn_x, spawn_y, len(self.bees), self, self.entity_list)
            self.bees.append(new_bee) # add to hive bee list
            self.entity_list.append(new_bee) # add bee to global(?) entity list

            return new_bee
        return None


    def update(self):
        """manage hive logic - honey use + growth, spawning new bees, updating own bees"""
        if self.honey_count > 10 and len(self.bees) < MAX_CAPACITY: # bee spawn timer thing
            self.spawn_timer += 1
            if self.spawn_timer >= BEE_SPAWN_INTERVAL:
                self.create_bee()
                self.honey_count -= 2  # use honey
                self.spawn_timer = 0   # reset timer