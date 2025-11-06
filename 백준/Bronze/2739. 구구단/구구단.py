import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
for i in range(1,10):
    print(f"{N} * {i} = {N * i}")