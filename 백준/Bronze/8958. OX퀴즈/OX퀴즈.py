import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    a = 0
    score = 0
    N = list(input())
    for i in range(len(N)):
        if N[i] == 'O':
            a += 1
            score += a
        else:
            a = 0
    print(score)
