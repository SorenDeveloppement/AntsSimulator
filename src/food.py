import pygame

from constants import Colors


class Food:
    def __init__(self, x: int, y: int, food_coef: int) -> None:
        self.x = x
        self.y = y
        self.food_coef = food_coef

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, Colors.DARK_GREEN.value, (self.x, self.y), 10)

    def decrease_food_coef(self) -> None:
        self.food_coef -= 1

        if self.food_coef <= 0:
            del self

    def get_location(self) -> tuple[int, int]:
        return self.x, self.y

    def get_food_coef(self) -> int:
        return self.food_coef

    def set_food_coef(self, f_coef: int) -> None:
        self.food_coef = f_coef

        if self.food_coef <= 0:
            del self
