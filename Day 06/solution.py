import numpy as np

x = []
y = []
for l in open('input.txt'):
    cx, cy = l.strip().split(", ")
    x.append(int(cx))
    y.append(int(cy))

max_x = max(x)
max_y = max(y)
grid = [[0 for i in range(0,max_x+100)] for j in range(0,max_y+100)]

for j in range(len(grid)):
    for i in range(len(grid[0])):
        dists = 0
        for z in range(len(x)):
            dists += (abs(y[z]-j)+abs(x[z]-i))
        if dists < 10000:
            grid[j][i] = 1

print sum(map(sum,grid))


lbl = range(1,len(x)+1)
x = [i-min(x) for i in x]
y = [i-min(y) for i in y]
max_x = max(x)
max_y = max(y)

grid = [[0 for i in range(0,max_x+1)] for j in range(0,max_y+1)]

for i in range(len(x)):
    grid[y[i]][x[i]] = lbl[i]

for j in range(len(grid)):
    for i in range(len(grid[0])):
        if grid[j][i] == 0:
            dists = []
            for z in range(len(x)):
                dists.append(abs(y[z]-j)+abs(x[z]-i))
            count = 0
            md = min(dists)
            for d in dists:
                if d==md:
                    count += 1
            if count == 1:
                grid[j][i] = lbl[np.argmin(dists)]
                

exclude = set()
for i in range(len(grid)):
    exclude.add(grid[i][0])
    exclude.add(grid[i][len(grid[0])-1])
for i in range(len(grid[0])):
    exclude.add(grid[0][i])
    exclude.add(grid[len(grid)-1][i])

max_area = 0
for q in lbl:
    if q not in exclude:
        area = sum(x.count(q) for x in grid)
        if area > max_area:
            max_area = area

print max_area