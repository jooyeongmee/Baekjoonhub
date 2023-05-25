import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
heights = list(map(int, sys.stdin.readline().rstrip().split()))

arr = []
for i in range(1, n):
    arr.append(heights[i] - heights[i-1])

arr.sort(reverse=True)
print(sum(arr[(k-1):]))