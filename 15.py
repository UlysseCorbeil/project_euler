import numpy as np

def c_path (n):
    grid = np.zeros([n + 1, n + 1])
    paths = 1

    # base case
    for k in range(len(grid)):
        grid[k, n] = 1
        grid[n, k] = 1

    # dynamic allocation for traversing
    for i in range(len(grid) - 1):
        for k in range(len(grid[i]) - 1):
            grid[i, k] = grid[i + 1, k] + grid[i, k + 1]

    # find path with binomial coefficients
    for k in range(0, n):
        paths *= (2 * n) - k
        paths /= k + 1

    return paths

print(c_path(20))
