import re

def whichApply(before,action,after):
    applied = []
    C = after[action[3]]
    regA = action[1] < 4
    regB = action[2] < 4

    if set_v(action[1],C):
        applied.append('seti')

    if regA:
        A = before[action[1]]
        B = action[2]
        if add(A,B,C):
            applied.append('addi')
        if mul(A,B,C):
            applied.append('muli')
        if ban(A,B,C):
            applied.append('bani')
        if bor(A,B,C):
            applied.append('bori')
        if set_v(A,C):
            applied.append('setr')
        if gt(A,B,C):
            applied.append('gtri')
        if eq(A,B,C):
            applied.append('eqri')

    if regA and regB:
        A = before[action[1]]
        B = before[action[2]]
        if add(A,B,C):
            applied.append('addr')
        if mul(A,B,C):
            applied.append('mulr')
        if ban(A,B,C):
            applied.append('banr')
        if bor(A,B,C):
            applied.append('borr')
        if gt(A,B,C):
            applied.append('gtrr')
        if eq(A,B,C):
            applied.append('eqrr')
    
    if regB:
        A = action[1]
        B = before[action[2]]
        if gt(A,B,C):
            applied.append('gtir')
        if eq(A,B,C):
            applied.append('eqir')

    return applied



def add(A, B, C):
    return (A + B) == C

def mul(A, B, C):
    return (A * B) == C

def ban(A, B, C):
    return (A & B) == C

def bor(A, B, C):
    return (A | B) == C

def set_v(A, C):
    return A == C

def gt(A,B,C):
    return (A > B and C == 1) or (A <= B and C == 0)

def eq(A,B,C):
    return (A == B and C == 1) or (A != B and C == 0)


numAbove3 = 0
whichFunction = {}
certain = [None for _ in range(16)]
device = [0, 0, 0, 0]
with open("input.txt") as fp:
    i = 0
    before = None
    action = None
    after = None
    for line in fp:
        l = i % 4
        if l == 0:
            if line[0] != 'B':
                break
            before = [int(x) for x in re.split('\[|\]|,',line.strip())[1:5]]
        elif l == 1:
            action = [int(x) for x in line.strip().split()]
        elif l == 2:
            after = [int(x) for x in re.split('\[|\]|,',line.strip())[1:5]]
        else:
            poss = whichApply(before,action,after)
            num = action[0]

            if len(poss) > 2:
                numAbove3 += 1
            
            if num not in whichFunction:
                whichFunction[num] = poss
            elif len(whichFunction[num]) > len(poss):
                whichFunction[num] = poss
        i+=1

    matched = False

    while not matched:
        for k in whichFunction.keys():
            if len(whichFunction[k]) == 1:
                certain[k] = whichFunction[k][0]
            else:
                for c in certain:
                    if c in whichFunction[k]:
                        whichFunction[k].remove(c)
        if None not in certain:
            matched = True

    for line in fp:
        if line[0] != '\n':
            action = [int(x) for x in line.strip().split()]
            func =  certain[action[0]]
            if func == "addr":
                device[action[3]] = device[action[1]] + device[action[2]]
            elif func == "addi":
                device[action[3]] = device[action[1]] + action[2]
            elif func == "mulr":
                device[action[3]] = device[action[1]] * device[action[2]]
            elif func == "muli":
                device[action[3]] = device[action[1]] * action[2]
            elif func == "banr":
                device[action[3]] = device[action[1]] & device[action[2]]
            elif func == "bani":
                device[action[3]] = device[action[1]] & action[2]
            elif func == "borr":
                device[action[3]] = device[action[1]] | device[action[2]]
            elif func == "bori":
                device[action[3]] = device[action[1]] | action[2]
            elif func == "setr":
                device[action[3]] = device[action[1]]
            elif func == "seti":
                device[action[3]] = action[1]
            elif func == 'gtir':
                if action[1] > device[action[2]]:
                    device[action[3]] = 1
                else:
                    device[action[3]] = 0
            elif func == 'gtri':
                if device[action[1]] > action[2]:
                    device[action[3]] = 1
                else:
                    device[action[3]] = 0
            elif func == 'gtrr':
                if device[action[1]] > device[action[2]]:
                    device[action[3]] = 1
                else:
                    device[action[3]] = 0
            elif func == 'eqir':
                if action[1] == device[action[2]]:
                    device[action[3]] = 1
                else:
                    device[action[3]] = 0
            elif func == 'eqri':
                if device[action[1]] == action[2]:
                    device[action[3]] = 1
                else:
                    device[action[3]] = 0
            elif func == 'eqrr':
                if device[action[1]] == device[action[2]]:
                    device[action[3]] = 1
                else:
                    device[action[3]] = 0

print numAbove3
print device