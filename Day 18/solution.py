import numpy as np
grid = []
for l in open("input.txt"):
    grid.append([x for x in l.strip()])
grid = np.array(grid)

grid2 = grid.copy()

vals = []
for _ in range(2000):

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            adj = [-1,0,1]
            if grid[y][x] == '.':
                numTree=0
                for i in adj:
                    for j in adj:
                        if y+i < 0 or x+j < 0 or y+i >= len(grid) or x+j >= len(grid[0]):
                            pass
                        elif grid[y+i][x+j] == '|':
                            numTree += 1
                if numTree >= 3:
                    grid2[y][x] = '|'
            if grid[y][x] == '|':
                numLY=0
                for i in adj:
                    for j in adj:
                        if y+i < 0 or x+j < 0 or y+i >= len(grid) or x+j >= len(grid[0]):
                            pass
                        elif grid[y+i][x+j] == '#':
                            numLY += 1
                if numLY >= 3:
                    grid2[y][x] = '#'
            if grid[y][x] == '#':
                remain = {'|': False, '#': False}
                for i in adj:
                    for j in adj:
                        if y+i < 0 or x+j < 0 or y+i >= len(grid) or x+j >= len(grid[0]):
                            pass
                        elif i == 0 and j == 0:
                            pass
                        elif grid[y+i][x+j] == '#':
                            remain['#'] = True
                        elif grid[y+i][x+j] == '|':
                            remain['|'] = True
                if False in remain.values():
                    grid2[y][x] = '.'
    grid = grid2.copy()

    woods = 0
    lys = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '|':
                woods += 1
            elif grid[i][j] == '#':
                lys += 1
    vals.append([lys*woods])

vals = np.array(vals)
i = 0
found = False
while not found:
    i += 1
    impvals = vals[i:]-vals[:-i]
    if sum(impvals[-i:]) == 0:
        found = True
print(i)
yrs = (1000000000 - 2001) % i
print(vals[-(i-yrs)])
#print(lys, woods, woods*lys)