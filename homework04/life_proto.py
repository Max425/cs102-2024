import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

        # Инициализация клеток
        self.grid = self.create_grid(randomize=True)

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def create_grid(self, randomize: bool = False) -> Grid:
        """Создание матрицы клеток"""
        grid: Grid = []
        for _ in range(self.cell_height):
            row = [random.randint(0, 1) if randomize else 0 for _ in range(self.cell_width)]
            grid.append(row)
        return grid

    def draw_grid(self) -> None:
        """Отрисовка клеток на экране"""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = pygame.Color("green") if cell else pygame.Color("white")
                rect = (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color, rect)

    def get_neighbours(self, cell: Cell) -> Cells:
        """Вернуть список соседних клеток"""
        x, y = cell
        neighbours = []
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.cell_width and 0 <= ny < self.cell_height:
                    neighbours.append(self.grid[ny][nx])
        return neighbours

    def get_next_generation(self) -> Grid:
        """Обновление состояния клеток"""
        new_grid: Grid = []
        for y in range(self.cell_height):
            new_row: Cells = []
            for x in range(self.cell_width):
                cell = self.grid[y][x]
                neighbours = self.get_neighbours((x, y))
                live_count = sum(neighbours)
                if cell == 1:
                    # Выживает с 2 или 3 соседями
                    new_row.append(1 if live_count in (2, 3) else 0)
                else:
                    # Появляется новая клетка с 3 соседями
                    new_row.append(1 if live_count == 3 else 0)
            new_grid.append(new_row)
        return new_grid

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()

            pygame.display.flip()
            self.grid = self.get_next_generation()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    game = GameOfLife(320, 240, 20)
    game.run()
