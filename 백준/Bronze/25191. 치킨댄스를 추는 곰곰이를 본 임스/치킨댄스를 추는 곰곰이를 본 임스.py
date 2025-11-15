import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
A,B = map(int, input().split())

a = A // 2
b = B // 1

if a+b > N:
    print(N)
else:
    print(a+b)
