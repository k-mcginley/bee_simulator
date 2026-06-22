import random
from entity import Entity
from bee import Bee
from config import *

class Beehive(Entity):

    num_beehives = 0
    beehive_img = "" # make later

    def __init__(self, x, y, starting_honey_count):
        super().__init__(x, y, Beehive.beehive_img)
        self._id = Beehive.num_beehives
        self.population = 0
        self.larva_count = 0
        self.honey_count = starting_honey_count
        self.bee_count = 0
        self.bees = []

    def create_bee(self):
        self._bees.append(Bee(0, 0, self._bee_count))
        self._bee_count += 1


