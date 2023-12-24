import pygame

from ant import Ant
from pheromone import Pheromone
from constants import Default, Colors


class Anthill:
    def __init__(self, x: int, y: int, pheromone: Pheromone) -> None:
        self.x = x
        self.y = y
        self.colony_pheromone: Pheromone = pheromone
        self.ants_number: int = Default.COLONY_SIZE.value
        self.ants: list[Ant] = []

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, Colors.BLUE.value, (self.x, self.y), 20)
