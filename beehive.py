import random
from entity import Entity
from bee import Bee

class Beehive(Entity):

    num_beehives = 0
    beehive_img = "" # make later

    # constraints: 
    MAX_POPULATION = 500
    MAX_FLYING = 100
    MAX_HONEY_COUNT = 200

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


