import random as r

import pygame

from ant import Ant
from anthill import Anthill
from constants import Default, Colors
from pheromone import Pheromone, PathPheromone, PheromoneType

pygame.init()

screen = pygame.display.set_mode((Default.WIDTH.value, Default.HEIGHT.value))
pygame.display.set_caption("Ant Simulation - SorenDeveloppement")

anthill: Anthill = Anthill(100, 100, Pheromone())
ant: Ant = Ant(150, 150, Pheromone())
pheromones: list[PathPheromone] = []


def update_ant():
    ant.walk()
    if r.randint(1, 10) == 6:
        ant.turn_left(r.randint(1, 2)) if r.randint(1, 2) == 1 else ant.turn_right(r.randint(1, 2))

    if ant.x >= Default.WIDTH.value:
        ant.turn_left(180 - ant.get_angle())
    elif ant.y <= 0 or ant.y >= Default.HEIGHT.value or ant.x <= 10:
        ant.turn_right(180 - ant.get_angle())

    ant.draw(screen)

    if ant.pheromone_delay == 0:
        pheromones.append(PathPheromone((0, 0, 0), PheromoneType.HOME_PATH, ant.x, ant.y))
        ant.pheromone_delay = Default.PHEROMONE_DELAY.value
    else:
        ant.pheromone_delay -= 1


def update_pheromones():
    for p in pheromones:
        if p.duration == 0:
            pheromones.pop(pheromones.index(p))
        else:
            p.draw(screen)
            p.duration -= 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            ...

    if pygame.key.get_pressed()[pygame.K_UP]:
        ant.walk()
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        ant.turn_right()
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        ant.turn_left()

    anthill.draw(screen)
    update_ant()
    update_pheromones()

    pygame.display.update()
    screen.fill(Colors.BLACK.value)
    pygame.time.Clock().tick(Default.TICKS.value)
