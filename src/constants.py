from enum import Enum


class Colors(Enum):
    BLACK: tuple[int, int, int] = (0, 0, 0)
    WHITE: tuple[int, int, int] = (255, 255, 255)
    RED: tuple[int, int, int] = (255, 0, 0)
    GREEN: tuple[int, int, int] = (0, 255, 0)
    BLUE: tuple[int, int, int] = (0, 0, 255)


class Default(Enum):
    WIDTH: int = 1200
    HEIGHT: int = 800
    TICKS = 120
    COLONY_SIZE = 15
    ANT_SPEED = 2
    ANGLE_SPEED = 1
    HOME_PHEROMONE_DURATION = 60 * TICKS
    FOOD_PHEROMONE_DURATION = 60 * TICKS
    NO_MORE_FOOD_PHEROMONE_DURATION = 30 * TICKS
    DANGER_PHEROMONE_DURATION = 40 * TICKS
    PHEROMONE_DELAY: int = 15
