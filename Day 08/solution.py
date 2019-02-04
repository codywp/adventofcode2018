import numpy as np

tree = []
for l in open('input.txt'):
    tree = [int(x) for x in l.strip().split(' ')]


def breakTree(tree):
    children, meta = tree[:2]
    tree = tree[2:]
    totals = 0
    nodes = {}

    for i in range(children):
        total, t2, tree = breakTree(tree)
        totals += total
        nodes[i+1] = t2

    totals += sum(tree[:meta])

    if children == 0:
        return totals, totals, tree[meta:]
    else:
        new_total = 0
        for x in tree[:meta]:
            new_total += nodes.get(x,0)
        return totals, new_total, tree[meta:]

total, root_val, remaining = breakTree(tree)
print total
print root_val