def count_move(grid, rows, cols):
    grid[0][0] = 1

    return count_top_down(grid, rows - 1, cols - 1)


def count_top_down(grid, row, col):
    print(row,col)
    if row < 0 or col < 0 or grid[row][col] == -1:
        return 0

    if grid[row][col] > 0:
        return grid[row][col]

    return count_top_down(grid, row - 1, col) + count_top_down(grid, row, col - 1)


