import sys

def input(): return sys.stdin.readline().rstrip()

a,b = map(int, input().split())


if a > b:
    for i in range(1,b+1):
        if (a % i == 0) & (b % i == 0):
            print(i, a // i, b // i)

else:
    for j in range(1,a+1):
        if (a % j == 0) & (b % j == 0):
            print(j, a // j, b // j)