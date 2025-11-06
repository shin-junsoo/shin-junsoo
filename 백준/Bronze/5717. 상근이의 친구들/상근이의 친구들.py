import sys

def input(): return sys.stdin.readline().rstrip()

while True:
    M,F = map(int,input().split())
    if M == 0 and F == 0:
        break

    print(M+F)