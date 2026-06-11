from beehive import Beehive
from entity import Entity

class Bee(Entity):

    bee_size = 5
    NECTAR_LIMIT = 10


    def __init__(self, id):
        self._id = id
        self._x = 0
        self._y = 0
        self._speed = 1
        self._beehive = Beehive()
        self._nectar_count = 0

    def move(self):
        pass
