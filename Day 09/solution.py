from collections import deque

num_players = 424
last = 71144
#for l in open('input.txt'):
#    arrayyyyy = l.strip().split(' ')

game = deque([0])
scores = [0 for _ in range(num_players)]

for l in [last, last*100]:
    for i in range(1,l+1):
        curr_player = i % num_players
        if i % 23 == 0:
            game.rotate(8) #8 instead of 7 because already pre-rotated
            scores[curr_player] += i + game.pop()
            game.rotate(-2) #reset to next location
        else:
            game.append(i)
            game.rotate(-1)

    print max(scores)