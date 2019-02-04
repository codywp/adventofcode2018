import numpy as np

cloth = np.zeros((1000,1000), dtype=np.int)

for line in open("input.txt"):
    l = line.strip().split("@ ")[1].split(': ')
    y, x = [int(q) for q in l[0].split(",")]
    h, w = [int(q) for q in l[1].split('x')]
    cloth[y:y+h,x:x+w] += 1
print np.sum(np.where(cloth > 1, 1, 0))

for line in open("input.txt"):
    l = line.strip().split("@ ")[1].split(': ')
    y, x = [int(q) for q in l[0].split(",")]
    h, w = [int(q) for q in l[1].split('x')]
    if np.sum(cloth[y:y+h,x:x+w]) == h*w:
        print line.split(" @")[0]