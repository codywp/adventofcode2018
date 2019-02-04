import numpy as np
import sys
#import png
sys.setrecursionlimit(4000)

def buildGrid(grid,vals):
    single = vals[0].split('=')
    double = [int(x) for x in vals[1].split('=')[1].split('..')]
    if single[0] == 'y':
        grid[int(single[1]),double[0]-300:double[1]-299] = '#'
    else:
        grid[double[0]:double[1]+1,int(single[1])-300] = '#'

def trapped(grid,loc):
    x,y = loc
    foundLWall = False
    foundRWall = False
    i = 0
    while not foundRWall:
        if grid[y+1][x+i] not in '#~':
            return False
        if grid[y][x+i] == '#':
            foundRWall = True
        i+=1

    i = 0
    while not foundLWall:
        if grid[y+1][x-i] not in '#~':
            return False
        if grid[y][x-i] == '#':
            foundLWall = True
        i+=1

    return True

def fill(grid,loc):
    x, y = loc
    i = 0
    while grid[y][x+i] != '#':
        grid[y][x+i] = '~'
        i += 1

    i = 1
    while grid[y][x-i] != '#':
        grid[y][x-i] = '~'
        i += 1

def flow(grid,loc):
    x,y = loc
    if y >= 2053:
        return
    if grid[y+1][x] == '.':
        grid[y+1][x] = '|'
        flow(grid,[x,y+1])
    if grid[y+1][x] in '#~':
        if grid[y][x+1] == '.':
            grid[y][x+1] = '|'
            flow(grid,[x+1,y])
        if grid[y][x-1] == '.':
            grid[y][x-1] = '|'
            flow(grid,[x-1,y])
    if trapped(grid,loc):
        fill(grid,loc)

grid =  np.array([['.' for _ in range(300,601)] for _ in range(2054)], dtype=str)

for line in open('input.txt'):
    vals = line.strip().split(',')
    buildGrid(grid,vals)

grid[0][200] = '+'

flow(grid,[200,0])

s = grid.shape


water = 0
for j in range(8,s[0]):
    for i in range(s[1]):
        if grid[j][i] in '|~':
            water+=1
print(np.sum(np.where(grid=='~')))
print(water)

"""
grid2 = np.zeros((s[0],s[1]*3))
for i in range(s[0]):
    for j in range(s[1]):
        z=j*3
        if grid[i][j]=='|':
            grid2[i][z:z+3] = [0,100,190]
        elif grid[i][j]=='#':
            grid2[i][z:z+3] = [250,190,0]
        elif grid[i][j]=='~':
            grid2[i][z:z+3] = [0,0,190]
        elif grid[i][j]=='.':
            grid2[i][z:z+3] = [80,0,80]
        elif grid[i][j]=='+':
            grid2[i][z:z+3] = [80,180,80]

f = open("final_water.png","wb")
w = png.Writer(301,2054)
w.write(f,grid2)
f.close()
"""
