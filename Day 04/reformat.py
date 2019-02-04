import numpy as np

csv = open("input.csv", 'w')
csv.write("Date,Time,Action\n")

for line in open("input.txt"):
    l = line.strip().lstrip('[q').split("] ")
    l[0] = l[0].split(' ')
    if l[1][0] == "G":
        l[1] = l[1].split(" ")[1]
    elif l[1][0] == 'w':
        l[1] = -1
    else:
        l[1] = 1
    l2 = "{0},{1},{2}\n".format(l[0][0],l[0][1],l[1])
    csv.write(l2)