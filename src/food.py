import pygame
from constants import Default, Colors

class Food:
    def __init__(self, x: int, y: int, food_coef: int) -> None:
        self.x = x
        self.y = y
        self.food_coef = food_coef
