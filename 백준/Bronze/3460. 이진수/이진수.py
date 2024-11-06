import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    result = []
    while n > 0:
        result.append(n % 2)
        n = n // 2

    for i in range(len(result)):
        if result[i] == 1:
            if i == len(result) - 1:
                print(i)
            else:
                print(i, end=' ')
