class World:
    def __init__(self):
        self.__temp = input("Input the world's temperature: ")
        self.__humidity = input("Input the world's humidity level: ")
        self.__air_pollution = int(input("Input the world's air pollution: "))
        self.__num_beehives = int(input("Input the starting number of beehives: "))
        self.__num_flowers = int(input("Input the number of flowers: "))
        self.__entities = []

        # pygame
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Pygame Window")

        # constraints:
        self.__MAX_BEES = 10000

        

        