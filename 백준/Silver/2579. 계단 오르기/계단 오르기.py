import sys

num = int(sys.stdin.readline())
stairs = [-1]
dp = [0] * (num + 1)
for _ in range(num):
    stairs.append(int(sys.stdin.readline()))

if num >= 1:
    dp[1] = stairs[1]
if num >= 2:
    dp[2] = stairs[1] + stairs[2]

for i in range(3, num+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[num])