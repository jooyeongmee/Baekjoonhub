import sys

n = int(input())
data = [-1]
dp = [0] * (n + 1)
for _ in range(n):
    data.append(int(sys.stdin.readline()))

dp[1] = data[1]
if n >= 2:
    dp[2] = data[1] + data[2]
if n >= 3:
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])

print(dp[-1])