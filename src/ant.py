import pygame
import math

from constants import Default, Colors
from pheromone import Pheromone


class Ant:
    def __init__(self, x: int, y: int, pheromone: Pheromone) -> None:
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = Default.ANT_SPEED.value()
        self.pheromone = pheromone

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, Colors.WHITE.value(), (self.x, self.y), 5)

    def walk(self) -> None:
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def turn_left(self) -> None:
        self.angle += Default.ANGLE_SPEED.value()

    def turn_right(self) -> None:
        self.angle -= Default.ANGLE_SPEED.value()
