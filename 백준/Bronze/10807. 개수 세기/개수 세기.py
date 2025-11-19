import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
num = list(map(int,input().split()))
V = int(input())

count = 0
for i in num:
    if i == V:
        count += 1

print(count)
