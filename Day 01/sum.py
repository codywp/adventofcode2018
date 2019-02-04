import numpy as np

txtfile = np.loadtxt("input.txt")
iter_offset = int(sum(txtfile))
print iter_offset
for i in range(1,len(txtfile)):
    txtfile[i] += txtfile[i-1]

freq = {}
for i in range(0,iter_offset):
    freq.setdefault(i,[])

for x in txtfile[:]:
    mod = x % iter_offset
    freq[mod].append(x)

mindiff = 9999999999
vals = []
for i in range(0,iter_offset):
    if len(freq[i]) > 1:
        diff = abs(freq[i][1] - freq[i][0])
        if diff < mindiff:
            mindiff = diff
            vals = [freq[i][0]]
        elif diff == mindiff:
            vals.append(freq[i][0])

for x in txtfile:
    if x in vals:
        print x+mindiff
        break