import pygame
import constants as c

pygame.init()

screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Ant Simulation - SorenDeveloppement")


def main():
    ...


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
    screen.fill(c.BLACK)
