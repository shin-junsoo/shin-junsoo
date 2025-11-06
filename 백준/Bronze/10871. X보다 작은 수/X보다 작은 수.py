import sys

def input(): return sys.stdin.readline().rstrip()

a,b = map(int, input().split())
count = []

for _ in range(a):
    N = list(map(int,input().split()))
    for i in range(len(N)):
        if N[i] < b:
            count.append(N[i])
            
print(*count) 