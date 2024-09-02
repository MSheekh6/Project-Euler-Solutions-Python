import math

def lattice_paths(grid_size):
    return math.comb(2 * grid_size, grid_size)


grid_size = 20

result = lattice_paths(grid_size)

print(result)
