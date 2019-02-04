from matplotlib import pyplot as plt
import numpy as np
import re

points = []
velocity = []
for l in open('input.txt'):
    point = re.split('<|>|,',l.strip())
    points.append([int(point[1]),int(point[2])])
    velocity.append([int(point[4]),int(point[5])])

points = np.array(points)
velocity = np.array(velocity)

t=0
while True:
    t += 1
    points = np.add(points,velocity)
    no_separate = True
    mapping = {}
    for x, y in points:
        mapping[(x,y)] = True
    for x, y in mapping:
        if not any((x + delta, y + delta2) in mapping for delta in xrange(-1, 2) for delta2 in xrange(-1, 2) if (delta, delta2) != (0, 0)):
            no_separate = False
            break
    if no_separate:
        print t
        plt.scatter(points[:,0],points[:,1])
        plt.gca().invert_yaxis()
        plt.show()
        exit()
