import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

count = 0
for i in range(1,N+1):
    a = list(str(i))
    for j in range(len(a)):
        if int(a[j]) == 3:
            count += 1
        elif int(a[j]) == 6:
            count += 1
        elif int(a[j]) == 9:
            count += 1
print(count)