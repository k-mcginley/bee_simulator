
from entity import Entity
from config import *
import pygame

class Bee(Entity):

    bee_size = 5
    bee_imgs = ["assets/bee_right.png", "assets/bee_down.png", "assets/bee_left.png", "assets/bee_up.png"]


    def __init__(self, x, y, id, beehive):
        super().__init__(x, y, Bee.bee_imgs[0])
        self.speed = 1
        self.beehive = beehive
        self.nectar_count = 0
        self.id = id

        self.direction = "right"
        self.min_axis_distance = 50
        self.current_axis = None
        self.distance_traveled = 0


    def move_towards(self, target_pos):
        target_x, target_y = target_pos
        center_x, center_y = self.rect.center

        distance_x = target_x - center_x
        distance_y = target_y - center_y

        tolerance = self.speed

        if abs(distance_x) <= tolerance and abs(distance_y) <= tolerance:
            self.rect.center = (target_x, target_y)
            self.current_axis = None
            self.distance_traveled = 0
            return

        if self.current_axis == None or self.distance_traveled >= self.min_axis_distance:
            can_switch_axis = True
        else:
            can_switch_axis = False

        if can_switch_axis:
            if self.current_axis == "x" and abs(distance_y) > abs(distance_x) and abs(distance_y) > tolerance:
                self.current_axis = "y"
                self.distance_traveled = 0
            elif self.current_axis == "y" and abs(distance_x) > abs(distance_y) and abs(distance_x) > tolerance:
                self.current_axis = "x"
                self.distance_traveled = 0
            elif self.current_axis == None:
                if abs(distance_x) >= abs(distance_y):
                    self.current_axis = "x"
                else:
                    self.current_axis = "y"

        if self.current_axis == "x" and abs(distance_x) <= tolerance and abs(distance_y) > tolerance:
            self.current_axis = "y"
            self.distance_traveled = 0
        elif self.current_axis == "y" and abs(distance_y) <= tolerance and abs(distance_x) > tolerance:
            self.current_axis = "x"
            self.distance_traveled = 0

        
        if self.current_axis == "x":
            if abs(distance_x) > tolerance:
                if distance_x > 0:
                    self.direction = "right"
                    step = self.speed
                else:
                    self.direction = "left"
                    step = -self.speed
                self.rect.centerx += step
                self.distance_traveled += abs(step)
            else:
                self.rect.centerx = target_x

        elif self.current_axis == "y":
            if abs(distance_y) > tolerance:
                if distance_y > 0:
                    self.direction = "up"
                    step = self.speed
                else:
                    self.direction = "down"
                    step = -self.speed
                self.rect.centery += step
                self.distance_traveled += abs(step)
            else:
                self.rect.centery = target_y

        
    def update(self): # change so that targt can change
        hive_target = (self.beehive.x, self.beehive.y)
        self.move_towards(hive_target)

        # fix bee facing direction