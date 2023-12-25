import pygame

from constants import Default, Colors
from anthill import Anthill
from ant import Ant
from pheromone import Pheromone

pygame.init()

screen = pygame.display.set_mode((Default.WIDTH.value, Default.HEIGHT.value))
pygame.display.set_caption("Ant Simulation - SorenDeveloppement")

anthill: Anthill = Anthill(100, 100, Pheromone())
ant: Ant = Ant(150, 150, Pheromone())

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
        ant.turn_left(The)

    anthill.draw(screen)
    ant.draw(screen)

    pygame.display.update()
    screen.fill(Colors.BLACK.value)
    pygame.time.Clock().tick(Default.TICKS.value)
