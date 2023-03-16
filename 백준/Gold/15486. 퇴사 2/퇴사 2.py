import sys

n = int(input())
data = [-1]
dp = [0] * (n+1)
for i in range(n):
  day, pay = map(int, sys.stdin.readline().split())
  data.append((day, pay))
#print(data)

for i in range(n, 0, -1):
  if (i + data[i][0]) <= (n+1):
    dp[i] = data[i][1]
    next_idx = i + data[i][0]
    if next_idx <= n:
      dp[i] += dp[next_idx]
    if i+1 <= n and dp[i+1] > dp[i]:
      dp[i] = dp[i+1]
  else:
    if i+1 <= n:
      dp[i] = dp[i+1]
#print(dp)

print(max(dp))