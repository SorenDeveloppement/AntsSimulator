import pygame

from constants import Default, Colors
from anthill import Anthill
from ant import Ant
from pheromone import Pheromone

pygame.init()

screen = pygame.display.set_mode((Default.WIDTH.value(), Default.HEIGHT.value()))
pygame.display.set_caption("Ant Simulation - SorenDeveloppement")

anthill: Anthill = Anthill(100, 100, Pheromone())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            ...

    if pygame.key.get_pressed()[pygame.K_UP]:
        ...

    pygame.display.update()
    screen.fill(Colors.BLACK.value())
