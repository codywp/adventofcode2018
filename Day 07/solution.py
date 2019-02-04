import numpy as np

prereqs = {}
all_options = set()

for l in open('input.txt'):
    temp = l.strip().split(" ")
    pre = temp[1]
    post = temp[7]
    if post not in prereqs:
        prereqs[post] = [pre]
    else:
        prereqs[post].append(pre)
    all_options.add(pre)
    all_options.add(post)

order = []
all_options = sorted(all_options)

while len(order) < len(all_options):
    for k in all_options:
        if k in prereqs:
            if set(prereqs[k]).issubset(order) and k not in order:
                order.append(k)
                break
        else:
            if k not in order:
                order.append(k)
                break

final = ''.join(order)
print final

t = 0
h = [[None,0] for i in range(5)]
done = []
length = len(all_options)
while len(done) < length:
    i = 0
    while i < len(h):
        if h[i][0] == None:
            for k in all_options:
                if k not in done:
                    rt = 61 + ord(k) - ord('A')
                    if k not in prereqs:
                        h[i][0] = k
                        h[i][1] = t + rt
                        all_options.remove(k)
                        break
                    elif set(prereqs[k]).issubset(done):
                        h[i][0] = k
                        h[i][1] = t + rt
                        all_options.remove(k)
                        break
        elif t >= h[i][1]:
            done.append(h[i][0])
            h[i][0] = None
            i=0
        i += 1
    t+=1

print max(h)[1]