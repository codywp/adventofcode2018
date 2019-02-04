import numpy as np
import re

serialnum = 1788
grid = [[int(str(((i+10)*j+serialnum)*(i+10))[-3])-5 for i in range(1,301)] for j in range(1,301)]

grid_np = np.array(grid)


def convolve2d(grid, size):
    output = np.zeros_like(grid)
    for x in range(grid.shape[1]-size):
        for y in range(grid.shape[0]-size):
            output[y,x] = np.sum(grid[y:y+size,x:x+size])
    return output

cur_max = -999999999
max_size = None
coord = None
for i in range(1,301):
    conv_grid = convolve2d(grid_np, i)
    if i==3:
        coord = np.unravel_index(np.argmax(conv_grid), grid_np.shape)
        print coord[1]+1, coord[0]+1
    imax = np.max(conv_grid)
    if imax > cur_max:
        cur_max = imax
        max_size = i
        coord = np.unravel_index(np.argmax(conv_grid), grid_np.shape)
print coord[1]+1,coord[0]+1, max_size
