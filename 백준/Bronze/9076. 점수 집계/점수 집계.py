import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = list(map(int,input().split()))
    N.sort()
    N.pop(0)
    N.pop(-1)
    N.sort()
    if N[-1] - N[0] >= 4:
        print('KIN')
    else:
        print(sum(N))