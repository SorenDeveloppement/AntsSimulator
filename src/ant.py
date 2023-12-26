import math

import pygame

from constants import Default, Colors
from pheromone import Pheromone, PheromoneType


class Sensor:
    def __init__(self, x: int, y: int, size: int):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.circle(screen, Colors.RED.value, (self.x, self.y), self.size, 2)

    def detect(self, pheromone_type: PheromoneType, anthill):
        for p in anthill.collective_pheromones:
            if p.is_(pheromone_type):
                if math.sqrt((self.x - p.get_location()[0]) ** 2 + (self.y - p.get_location()[1]) ** 2) <= self.size:
                    return True

    def set_location(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_location(self) -> tuple[int, int]:
        return self.x, self.y


class Ant:
    def __init__(self, anthill: "Anthill", x: int, y: int, pheromone: Pheromone) -> None:
        self.anthill = anthill
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = Default.ANT_SPEED.value
        self.pheromone = pheromone
        self.home_pheromones = []
        self.pheromone_delay = Default.PHEROMONE_DELAY.value
        self.sensors: list[Sensor] = [
            Sensor(int(self.x + math.cos(math.radians(self.angle)) * 10),
                   int(self.y + math.sin(math.radians(self.angle)) * 10),
                   10)]

        self.found_food = False

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, Colors.WHITE.value, (self.x, self.y), 5)
        pygame.draw.line(screen, Colors.WHITE.value, (self.x, self.y),
                         (self.x + math.cos(math.radians(self.angle)) * 10,
                          self.y + math.sin(math.radians(self.angle)) * 10))

    def walk(self) -> None:
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.update_sensors()

    def turn_left(self, angle: int = None) -> None:
        if angle is None:
            self.angle += Default.ANGLE_SPEED.value
        else:
            self.angle += angle

        if self.angle < 0 or self.angle > 360:
            self.angle %= 360

    def turn_right(self, angle: int = None) -> None:
        if angle is None:
            self.angle -= Default.ANGLE_SPEED.value
        else:
            self.angle -= angle

        if self.angle < 0 or self.angle > 360:
            self.angle %= 360

    def update_sensors(self) -> None:
        for s in self.sensors:
            s.set_location(int(self.x + math.cos(math.radians(self.angle)) * 10),
                           int(self.y + math.sin(math.radians(self.angle)) * 10))

    def get_angle(self) -> int:
        return self.angle

    def set_angle(self, angle: int) -> None:
        self.angle = angle
