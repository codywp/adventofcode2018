

def gt(A,B,C):
    return A > B

def eq(A,B,C):
    return A == B


register = [0 for _ in range(6)]
instructions = []
ip = None
for l in open("input.txt"):
    line = l.strip()
    if line[0] == "#":
        ip = int(line.split()[1])
    else:
        line = line.split()
        instructions.append(line)

while register[ip] < len(instructions):
    instr = instructions[register[ip]]
    action = instr[0]
    vals = [int(instr[i]) for i in range(1,4)]
    if action[0:3] == 'add':
        if action[-1] == 'i':
            register[vals[2]] = register[vals[0]] + vals[1]
        else:
            register[vals[2]] = register[vals[0]] + register[vals[1]]
    elif action[0:3] == 'mul':
        if action[-1] == 'i':
            register[vals[2]] = register[vals[0]] * vals[1]
        else:
            register[vals[2]] = register[vals[0]] * register[vals[1]]
    elif action[0:3] == 'ban':
        if action[-1] == 'i':
            register[vals[2]] = register[vals[0]] & vals[1]
        else:
            register[vals[2]] = register[vals[0]] & register[vals[1]]
    elif action[0:3] == 'bor':
        if action[-1] == 'i':
            register[vals[2]] = register[vals[0]] | vals[1]
        else:
            register[vals[2]] = register[vals[0]] | register[vals[1]]
    elif action[0:2] == 'gt':
        if action[2:4] == 'rr':
            if register[vals[0]] > register[vals[1]]:
                register[vals[2]] = 1
            else:
                register[vals[2]] = 0
        elif action[2:4] == 'ri':
            if register[vals[0]] > vals[1]:
                register[vals[2]] = 1
            else:
                register[vals[2]] = 0
        else:
            if vals[0] > register[vals[1]]:
                register[vals[2]] = 1
            else:
                register[vals[2]] = 0
    elif action[0:2] == 'eq':
        if action[2:4] == 'rr':
            if register[vals[0]] == register[vals[1]]:
                register[vals[2]] = 1
            else:
                register[vals[2]] = 0
        elif action[2:4] == 'ri':
            if register[vals[0]] == vals[1]:
                register[vals[2]] = 1
            else:
                register[vals[2]] = 0
        else:
            if vals[0] == register[vals[1]]:
                register[vals[2]] = 1
            else:
                register[vals[2]] = 0
    elif action[0:3] == 'set':
        if action[-1] == 'i':
            register[vals[2]] = vals[0]
        else:
            register[vals[2]] = register[vals[0]]

    register[ip] += 1


print(register)