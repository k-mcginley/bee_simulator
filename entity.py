from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.img, self.rect)

    @abstractmethod
    def move(self):
        pass