import sys

input = sys.stdin.readline

n, k = map(int, input().split())
result = set()

for i in range(1, n+1):
    if n % i == 0:
        result.add(n // i)

result = list(result)
result.sort()

if len(result) >= k:
    print(result[k-1])
else:
    print(0)
    