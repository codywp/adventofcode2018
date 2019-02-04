
code_og = ""

for l in open('input.txt'):
    code_og = l.strip()

min_len = 999999999
for j in range(65,91):
    code = code_og.replace(chr(j),"")
    code = code.replace(chr(j+32),"")
    
    done = False
    i = 0
    prevLen = 0
    while not done:
        if i+1 < len(code):
            if abs(ord(code[i]) - ord(code[i+1])) == 32:
                if i+2 < len(code):
                    code = code[:i] + code[i+2:]
                    i -= 2
        else:
            if prevLen == len(code):
                done = True
            else:
                prevLen = len(code)
                i=0

        i += 1
        if i < 0:
            i = 0

    print chr(j), len(code)
    if len(code) < min_len:
        min_len = len(code)

print min_len