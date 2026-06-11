class World:
    def __init__(self, temp: float, humidity: int, air_pollution: int, num_beehives: int, num_flowers: int):
        self.__temp = temp
        self.__humidity = humidity
        self.__air_pollution = air_pollution
        self.__num_beehives = num_beehives
        self.__num_flowers = num_flowers
        self.__entities = []

        # constraints:
        self.__MAX_BEES = 10000

    