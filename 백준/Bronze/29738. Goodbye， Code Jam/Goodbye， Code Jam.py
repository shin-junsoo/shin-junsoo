import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())

b = []
for i in range(T):
    a = int(input())
    b.append(a)

for j in range(len(b)):
    if b[j] > 4500:
        print(f'Case #{j+1}: Round 1')
        continue
    elif b[j] > 1000:
        print(f'Case #{j+1}: Round 2')
        continue
    elif b[j] > 25:
        print(f'Case #{j+1}: Round 3')
    else:
        print(f'Case #{j+1}: World Finals')