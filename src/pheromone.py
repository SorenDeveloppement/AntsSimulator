from enum import Enum

import pygame.draw

from constants import Colors


class PheromoneType(Enum):
    HOME_PATH: int = 0
    FOOD_PATH: int = 1
    DANGER_PATH: int = 2
    NO_MORE_FOOD_PATH: int = 3


class Pheromone:
    def __init__(self, code: tuple[int, int, int] = (0, 0, 0)) -> None:
        self.code: tuple[int, int, int] = code

    def __eq__(self, other):
        return self.code == other.code


class PathPheromone(Pheromone):
    def __init__(self, code: tuple[int, int, int] = (0, 0, 0),
                 pheromone_type: PheromoneType = PheromoneType.HOME_PATH, x: int = 0, y: int = 0) -> None:
        super().__init__(code)
        self.type: PheromoneType = pheromone_type
        self.x = x
        self.y = y

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, Colors.BLUE.value, (self.x, self.y), 3)

    def _is(self, p_type: PheromoneType) -> bool:
        return self.type == p_type
