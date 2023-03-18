import sys

n = int(sys.stdin.readline().strip())
val = 9999999999
stones = []
dp = [0] + [val] * (n-1)

for i in range(n-1):
    s, b = map(int, sys.stdin.readline().strip().split())
    stones.append((s, b))

    if i + 1 < n:
        dp[i+1] = min(dp[i+1], dp[i]+s)
    if i + 2 < n:
        dp[i+2] = min(dp[i+2], dp[i]+b)

k = int(sys.stdin.readline().strip())
#매우 큰 점프를 사용하 때
min_energy = dp[-1]
for i in range(3, n):
    energy, dp1, dp2 = dp[i-3]+k, val, val
    for j in range(i, n-1):
        if i + 1 <= n:
            dp1 = min(dp1, energy + stones[j][0])
        if i + 2 <= n:
            dp2 = energy + stones[j][1]
        energy, dp1= dp1, dp2
    min_energy = min(min_energy, energy)

print(min_energy)
