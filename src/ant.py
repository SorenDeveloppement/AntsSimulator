import math
from enum import Enum

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
        for p in anthill:
            if p.is_(pheromone_type):
                if math.sqrt((self.x - p.get_location()[0]) ** 2 + (self.y - p.get_location()[1]) ** 2) <= self.size:
                    return True

    def detect_food(self, array: "Food") -> bool:
        for f in array:
            if math.sqrt((self.x - f.get_location()[0]) ** 2 + (self.y - f.get_location()[1]) ** 2) <= self.size:
                return True

    def set_location(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_location(self) -> tuple[int, int]:
        return self.x, self.y


class AntState(Enum):
    SEARCHING_FOOD = 0
    GO_TO_HOME = 1
    DANGER = 2
    BRINGING_FOOD = 3

    def is_(self, other: "AntState"):
        return self == other


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
        self.sensor_distance = 20
        self.sensors: list[Sensor] = []

        self.state = None

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, Colors.WHITE.value, (self.x, self.y), 5)
        pygame.draw.line(screen, Colors.WHITE.value, (self.x, self.y),
                         (self.x + math.cos(math.radians(self.angle)) * 10,
                          self.y + math.sin(math.radians(self.angle)) * 10))

    def walk(self) -> None:
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.update_sensors()

    def turn_left(self, angle: int | float = None) -> None:
        if angle is None:
            self.angle += Default.ANGLE_SPEED.value
        else:
            self.angle += angle

        if self.angle < 0 or self.angle > 360:
            self.angle %= 360

    def turn_right(self, angle: int | float = None) -> None:
        if angle is None:
            self.angle -= Default.ANGLE_SPEED.value
        else:
            self.angle -= angle

        if self.angle < 0 or self.angle > 360:
            self.angle %= 360

    def update_sensors(self) -> None:
        num_sensors = 7
        sensor_length = 5
        sensor_spacing = 25

        if not self.sensors:
            self.sensors = [Sensor(0, 0, sensor_length) for _ in range(num_sensors)]

        for i, sensor in enumerate(self.sensors):
            sensor_angle = self.angle + (i - (len(self.sensors) - 1) / 2) * sensor_spacing
            sensor_x = int(self.x + math.cos(math.radians(sensor_angle)) * self.sensor_distance)
            sensor_y = int(self.y + math.sin(math.radians(sensor_angle)) * self.sensor_distance)

            sensor.set_location(sensor_x, sensor_y)

    def follow_sensor(self, sensor: Sensor) -> None:
        sensor_coord = sensor.get_location()

        dx = sensor_coord[0] - self.x
        dy = sensor_coord[1] - self.y

        angle_to_sensor = math.degrees(math.atan2(dy, dx))
        angle_difference = angle_to_sensor - self.angle

        self.turn_left(angle_difference)

    def get_angle(self) -> int:
        return self.angle

    def get_state(self) -> AntState:
        return self.state

    def set_angle(self, angle: int) -> None:
        self.angle = angle

    def set_state(self, state: AntState) -> None:
        self.state = state
