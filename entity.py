from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, x, y, img):
        self._x = x
        self._y = y
        self.img = pygame.image.load(img).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.topleft = (self._x, self._y)

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    @abstractmethod
    def move(self):
        pass