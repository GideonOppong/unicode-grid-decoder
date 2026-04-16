def build_grid(points, max_x, max_y):
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in points:
        grid[y][x] = char

    return grid
