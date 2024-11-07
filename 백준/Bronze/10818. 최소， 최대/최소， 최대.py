import sys

input = sys.stdin.readline

n = int(input())
data = map(int, input().split())

min = 1000000
max = -1000000

for value in data:
    if value < min:
        min = value
    if value > max:
        max = value

print(min, max)
