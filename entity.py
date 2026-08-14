from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, x, y, img):
        #self.x = x
        #self.y = y
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    @property
    def x(self):
        return self.rect.centerx

    @property
    def y(self):
        return self.rect.centery

    def draw(self, screen):
        screen.blit(self.img, self.rect)


    @abstractmethod
    def update(self):
        pass
    