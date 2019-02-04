import numpy as np
import re

recipes = '209231'
scores = '37'
elf1 = 0
elf2 = 1

found = False
while not found:
    score1 = int(scores[elf1])
    score2 = int(scores[elf2])
    scores = scores + str(score1+score2)
    nogo = len(scores)
    elf1 = (elf1 + score1 + 1) % nogo
    elf2 = (elf2 + score2 + 1) % nogo
    rlen = len(recipes)
    if recipes == scores[-rlen:]:
        found = True
        print nogo-rlen
    elif recipes == scores[-rlen-1:-1]:
        found = True
        print nogo-rlen-1




"""
recipes = 209231
scores = '37'
elf1 = 0
elf2 = 1

nogo = 2
while nogo < recipes + 10:
    score1 = int(scores[elf1])
    score2 = int(scores[elf2])
    scores = scores + str(score1+score2)
    nogo = len(scores)
    elf1 = (elf1 + score1 + 1) % nogo
    elf2 = (elf2 + score2 + 1) % nogo

print scores[recipes:recipes+10]
"""