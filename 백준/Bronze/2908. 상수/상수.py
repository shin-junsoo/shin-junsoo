import sys

def input(): return sys.stdin.readline().rstrip()

a,b = map(int, input().split())

a1=str(a)[::-1]
b1=str(b)[::-1]

a2 = int(a1)
b2 = int(b1)

if a2 > b2:
    print(a2)
else:
    print(b2)
