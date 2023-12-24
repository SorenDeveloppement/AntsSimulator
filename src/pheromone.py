class Pheromone:
    def __init__(self, code: tuple[int, int, int] = (0, 0, 0)) -> None:
        self.code = code

    def __eq__(self, other):
        return self.code == other.code
