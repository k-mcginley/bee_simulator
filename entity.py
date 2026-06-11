from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        pass

    @abstractmethod
    def move(self):
        pass