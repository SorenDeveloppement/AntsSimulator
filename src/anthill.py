import pygame
import math

from ant import Ant
from constants import Default, Colors
from pheromone import Pheromone


class Anthill:
    def __init__(self, x: int, y: int, radius: int, pheromone: Pheromone) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.colony_pheromone: Pheromone = pheromone
        self.ants_number: int = Default.COLONY_SIZE.value
        self.ants: list[Ant] = []
        self.collective_pheromones: list = []
        self.food_count = 0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, Colors.BLUE.value, (self.x, self.y), self.radius)

    def drop_food(self, count) -> None:
        self.food_count += abs(count)

    def on_it(self, x: int, y: int) -> bool:
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2) <= self.radius
