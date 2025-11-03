import sys

def input(): return sys.stdin.readline().rstrip()

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:  # 입력 종료 조건
        break
    if a>b:
        print('Yes')
    else:
        print('No')