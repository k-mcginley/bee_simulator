import sys
import pygame

# 1. Initialize Pygame modules
pygame.init()

# 2. Game Constants
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
FPS = 60

# Color definitions (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 3. Set up the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Window")

# 4. Initialize the game clock
clock = pygame.time.Clock()


bee_img = pygame.image.load("assets/bee_image.png").convert_alpha()

character_rect = bee_img.get_rect()
character_rect.topleft = (0, 0)

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

        # --- Game Logic / State Updates ---
        # (Move players, check collisions, update scores here)

        # --- Drawing / Rendering Code ---
        # Clear screen with a background color
        screen.fill(BLACK)

        # (Draw your game sprites and shapes here)
        screen.blit(bee_img, character_rect)

        # Refresh the screen display
        pygame.display.flip()

        # --- Frame Rate Management ---
        # Limits the loop to the specified FPS
        clock.tick(FPS)

    # 6. Clean Up and Exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()