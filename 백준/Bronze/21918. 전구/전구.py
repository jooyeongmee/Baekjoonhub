import sys

n, m = map(int, sys.stdin.readline().split())
status = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        status[b] = c
    elif a == 2:
        for j in range(b, c+1):
            status[j] = status[j] ^ 1
    elif a == 3:
        for j in range(b, c+1):
            status[j] = 0
    elif a == 4:
        for j in range(b, c+1):
            status[j] = 1

for i in range(1, n+1):
    print(status[i], end=" ")