from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]

def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    x, y = coord
    directions = []
    if x > 1: directions.append((-2, 0))
    if y < len(grid[0]) - 2: directions.append((0, 2))
    if not directions: return grid
    dx, dy = choice(directions)
    grid[x + dx // 2][y + dy // 2] = " "
    return grid

def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    grid = create_grid(rows, cols)
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                remove_wall(grid,(x, y))

    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid

def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    return [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == "X"]

def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    rows, cols = len(grid), len(grid[0])
    new_grid = [row[:] for row in grid]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == k:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and (grid[ni][nj] == 0 or grid[ni][nj] == " "):
                        new_grid[ni][nj] = k + 1
    return new_grid

def shortest_path(grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    x, y = exit_coord
    if not isinstance(grid[x][y], int) or grid[x][y] == 0: return None
    path = [(x, y)]
    k = grid[x][y]
    while k > 1:
        cx, cy = path[-1]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == k - 1:
                path.append((nx, ny))
                k -= 1
                break
    return path

def solve_maze(grid: List[List[Union[str, int]]]) -> Tuple[List[List[Union[str, int]]], Optional[List[Tuple[int, int]]]]:
    exits = get_exits(grid)
    if len(exits) < 2: return grid, None
    start, end = exits[0], exits[1]
    dist_grid = [[0 if v in [" ", "X"] else v for v in row] for row in grid]
    dist_grid[start[0]][start[1]] = 1
    k = 1
    while dist_grid[end[0]][end[1]] == 0:
        next_grid = make_step(dist_grid, k)
        if next_grid == dist_grid: return grid, None
        dist_grid = next_grid
        k += 1
    return grid, shortest_path(dist_grid, end)


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
