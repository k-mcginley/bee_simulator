import sys
import pygame

from world import World
from beehive import Beehive
from flower import Flower

WIDTH = 800
HEIGHT = 500

pygame.init()

def main():
    world_temp = input("Input the world's temperature: ")
    world_humidity = input("Input the world's humidity level: ")
    world_pollution = int(input("Input the world's air pollution: "))
    starting_num_beehives = int(input("Input the starting number of beehives: "))
    num_flowers = int(input("Input the number of flowers: "))

    world = World(world_temp, world_humidity, world_pollution, starting_num_beehives, num_flowers)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game World")
clock = pygame.time.Clock()


running = True
while running:
    # Clear the background screen frame (fills with light blue sky color)
    screen.fill((135, 206, 235))
    
    # Check for quit window conditions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Draw the map grid on top of the background
    draw_world(screen, WORLD_MAP)
    
    # Refresh display and cap the framerate
    pygame.display.update()
    clock.tick(FPS)

# Clean termination
pygame.quit()
sys.exit()