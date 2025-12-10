import sys

def input(): return sys.stdin.readline().rstrip()

K,N,M = map(int, input().split())

if K*N-M > 0:
    print(K*N-M)
else:
    print(str(0))