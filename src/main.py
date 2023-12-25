import random as r

import pygame

from ant import Ant
from anthill import Anthill
from constants import Default, Colors
from pheromone import Pheromone, PathPheromone, PheromoneType

pygame.init()

screen = pygame.display.set_mode((Default.WIDTH.value, Default.HEIGHT.value))
pygame.display.set_caption("Ant Simulation - SorenDeveloppement")

anthill: Anthill = Anthill(Default.WIDTH.value / 2, Default.HEIGHT.value / 2, Pheromone())
for i in range(360):
    anthill.ants.append(Ant(anthill.x, anthill.y, Pheromone()))
    anthill.ants[i].set_angle(i)


def update_ant(ant: Ant):
    ant.walk()
    if r.randint(1, 10) == 6:
        ant.turn_left(r.randint(1, 5)) if r.randint(1, 2) == 1 else ant.turn_right(r.randint(1, 5))

    if ant.x >= Default.WIDTH.value:
        ant.turn_left(90)
    elif ant.x <= 0:
        ant.turn_left(90)
    elif ant.y >= Default.HEIGHT.value:
        ant.turn_left(90)
    elif ant.y <= 0:
        ant.turn_left(90)

    ant.draw(screen)

    if ant.pheromone_delay == 0:
        ant.home_pheromones.append(PathPheromone((0, 0, 0), PheromoneType.HOME_PATH, ant.x, ant.y))
        ant.pheromone_delay = Default.PHEROMONE_DELAY.value
    else:
        ant.pheromone_delay -= 1


def update_pheromones(draw_p: bool):
    for p in anthill.collective_pheromones:
        if p.duration == 0:
            anthill.collective_pheromones.pop(anthill.collective_pheromones.index(p))
        else:
            if draw_p:
                p.draw(screen)
            p.duration -= 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            ...

    anthill.draw(screen)
    update_pheromones(False)
    for ant in anthill.ants:
        update_ant(ant)

    pygame.display.update()
    screen.fill(Colors.BLACK.value)
    pygame.time.Clock().tick(Default.TICKS.value)
