import random

class Beehive(Entity):

    num_beehives = 0

    # constraints: 
    MAX_POPULATION = 500
    MAX_FLYING = 100
    MAX_HONEY_COUNT = 200

    def __init__(self, x, y, starting_honey_count):
        self._id = Beehive.num_beehives
        self._x = x
        self._y = y
        self._population = 0
        self._larva_count = 0
        self._honey_count = starting_honey_count
        self._bee_count = 0
        self._bees = []

    def create_bee(self):
        self._bees.append(Bee(self._bee_count))
        self._bee_count += 1


