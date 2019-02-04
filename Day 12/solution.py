import numpy as np

initial_state = None
matches = []
done = False
for l in open('input.txt'):
    if not done:
        initial_state = l.strip().split(' ')[2]
        done = True
    else:
        temp = l.strip().split(' ')
        if len(temp)>1:
            if temp[2] == '#':
                matches.append(temp[0])

num_gens = 150
offset = 350

gens = [['.' for _ in range(len(initial_state)+800)] for _ in range(num_gens)]
gens[0][offset:len(initial_state)+offset] = initial_state

for j in range(1,num_gens):
    for i in range(2,len(gens[0])-2):
        for match in matches:
            if ''.join(gens[j-1][i-2:i+3]) == match:
                gens[j][i] = '#'
                break
vals = []
for j in range(len(gens)):
    total = 0
    for i in range(len(gens[-1])):
        if gens[j][i] == '#':
            total += i - offset
    vals.append(total)

print vals[20]
print vals[149] + 78*(50000000000 - 149)