import sys

def input(): return sys.stdin.readline().rstrip()

R1, S = map(int, input().split())

R2 = 2*S-R1

print(R2)
           