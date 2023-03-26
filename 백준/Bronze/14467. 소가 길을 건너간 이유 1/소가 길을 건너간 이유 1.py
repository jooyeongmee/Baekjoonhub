import sys

n = int(sys.stdin.readline())
cows = {}
count = 0
for _ in range(n):
    cow, state = map(int, sys.stdin.readline().split())
    if cow in cows.keys() and cows[cow] != state:
        count += 1
    cows[cow] = state

print(count)