import random
from entity import Entity
from config import *

class Beehive(Entity):

    num_beehives = 0
    beehive_img = "assets/beehive_1.png"

    def __init__(self, x, y, starting_honey_count=50, max_capacity=100):
        super().__init__(x, y, Beehive.beehive_img)
        Beehive.num_beehives + 1
        self._id = Beehive.num_beehives

        self.larva_count = 5
        self.honey_count = starting_honey_count
        self.bees = []
        self.max_capacity = max_capacity

        self.spawn_timer = 0
        self.spawn_interval = 180


    def create_bee(self):
        if len(self.bees) < self.max_capacity:
            spawn_x = self.rect.centerx + random.randint(-10, 10)
            spawn_y = self.rect.centery + random.randint(-10, 10)
            
            new_bee = Bee(spawn_x, spawn_y, len(self.bees), self)
            self.bees.append(new_bee)
            return new_bee
        return None

    def update(self):
        """
        Runs every frame to manage hive simulation logic:
        1. Honey consumption / growth
        2. Spawning new bees over time
        3. Updating all bees associated with this hive
        """
        # 1. Automatic Bee Spawning Timer
        if self.honey_count > 10 and len(self.bees) < self.max_capacity:
            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_interval:
                self.create_bee()
                self.honey_count -= 2  # Spawning consumes hive honey
                self.spawn_timer = 0   # Reset timer

        # 2. Update all bees belonging to this hive
        for bee in self.bees:
            bee.update()