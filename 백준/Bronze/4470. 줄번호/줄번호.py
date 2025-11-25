import sys

def input(): return sys.stdin.readline().rstrip()

a = []
N = int(input())

for _ in range(N):
    a += input().split("\n")


for i in range(len(a)):
    print(str(i+1)+"." + " " + str(a[i]))