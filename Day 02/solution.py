double = 0
triple = 0
all_codes = []
for line in open("input.txt"):
    l = line.strip()
    all_codes.append(l)
    count = {}
    for c in l:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    for k, v in count.items():
        if v==2:
            double += 1
            break
    for k, v in count.items():
        if v==3:
            triple += 1
            break
print double * triple

for x in all_codes:
    for y in all_codes:
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                if diff == 1:
                    diff = 2
                    break
                else:
                    diff = 1
        if diff == 1:
            same_chars = ''
            for j in range(len(x)):
                if x[j] == y[j]:
                    print(x[j]),
            break