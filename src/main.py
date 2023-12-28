import random as r

import pygame

from ant import Ant, AntState
from anthill import Anthill
from constants import Default, Colors
from food import Food
from pheromone import Pheromone, PathPheromone, PheromoneType

pygame.init()
screen = pygame.display.set_mode((Default.WIDTH.value, Default.HEIGHT.value))
pygame.display.set_caption("Ant Simulation - SorenDeveloppement")

food: list[Food] = []
anthill: Anthill = Anthill(Default.WIDTH.value / 2, Default.HEIGHT.value / 2, 20, Pheromone())
for i in range(18):
    anthill.ants.append(Ant(anthill, anthill.x, anthill.y, Pheromone()))
    anthill.ants[i].set_angle(i)
    anthill.ants[i].set_state(AntState.SEARCHING_FOOD)


def update_ant(ant: Ant):
    ant.walk()

    ant.draw(screen)
    for s in ant.sensors:
        s.draw(screen)
        if (s.detect(PheromoneType.FOOD_PATH, anthill.collective_pheromones) and
                ant.get_state().is_(AntState.SEARCHING_FOOD)):
            ant.follow_sensor(s)
        elif s.detect(PheromoneType.HOME_PATH, ant.home_pheromones) and (
                ant.get_state().is_(AntState.BRINGING_FOOD) or ant.get_state().is_(AntState.GO_TO_HOME)):
            ant.follow_sensor(s)
        elif s.detect_food(food) and ant.get_state().is_(AntState.SEARCHING_FOOD):
            ant.set_state(AntState.BRINGING_FOOD)
            ant.turn_left(180)

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

    if ant.get_state().is_(AntState.SEARCHING_FOOD):
        if ant.pheromone_delay == 0:
            ant.home_pheromones.append(PathPheromone((0, 0, 0), PheromoneType.HOME_PATH, ant.x, ant.y))
            ant.pheromone_delay = Default.PHEROMONE_DELAY.value
        else:
            ant.pheromone_delay -= 1
    elif ant.get_state().is_(AntState.BRINGING_FOOD):
        if ant.pheromone_delay == 0:
            anthill.collective_pheromones.append(PathPheromone((0, 0, 0), PheromoneType.FOOD_PATH, ant.x, ant.y))
            ant.pheromone_delay = Default.PHEROMONE_DELAY.value
        else:
            ant.pheromone_delay -= 1
        if anthill.on_it(ant.x, ant.y):
            anthill.drop_food(1)
            ant.set_state(AntState.SEARCHING_FOOD)
            ant.turn_left(180)


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

    if pygame.mouse.get_pressed()[0]:
        anthill.collective_pheromones.append(
            PathPheromone((0, 0, 0), PheromoneType.FOOD_PATH, pygame.mouse.get_pos()[0],
                          pygame.mouse.get_pos()[1]))
    if pygame.mouse.get_pressed()[2]:
        food.append(Food(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1))

    anthill.draw(screen)
    for f in food:
        f.draw(screen)
    update_pheromones(False)
    for ant in anthill.ants:
        update_ant(ant)

    pygame.display.update()
    screen.fill(Colors.BLACK.value)
    pygame.time.Clock().tick(Default.TICKS.value)
