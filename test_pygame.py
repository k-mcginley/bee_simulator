import sys
import pygame

# 1. Initialize Pygame modules
pygame.init()

# 2. Game Constants
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800
FPS = 60
SPEED = 3

# Color definitions (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 3. Set up the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Window")

# 4. Initialize the game clock
clock = pygame.time.Clock()


bee_img = pygame.image.load("assets/bee_pixel.png").convert_alpha()
bee_img = pygame.transform.scale(bee_img, (20, 20))

rect = bee_img.get_rect()
rect.center = (100, 100)

def main():
    # Game state variable
    running = True

    # 5. Main Game Loop
    while running:

        # --- Event Handling Loop ---
        for event in pygame.event.get():
            # Check if user clicked the window's close button
            if event.type == pygame.QUIT:
                running = False

            # Example Keyboard input detection
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        mouse_pos = pygame.mouse.get_pos()

        # create vectors for the target and current center
        target = pygame.math.Vector2(mouse_pos)
        current = pygame.math.Vector2(rect.center)

        distance = current.distance_to(target)

        if distance > 0:
            if distance < SPEED:
                rect.center = mouse_pos
            else:
                direction = (target - current).normalize()
                new_pos = current + direction * SPEED
                rect.center = (int(new_pos.x), int(new_pos.y))


        # --- Drawing / Rendering Code ---
        screen.fill(WHITE)

        # draw game sprites and shapes here
        screen.blit(bee_img, rect)

        # refresh screen display
        pygame.display.flip()

        # --- Frame Rate Management ---
        # Limits the loop to the specified FPS
        clock.tick(FPS)


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()