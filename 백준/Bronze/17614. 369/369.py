import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

count = 0
for i in range(1,N+1):
    a = str(i)
    count += a.count('3') + a.count('6') + a.count('9')
print(count)
