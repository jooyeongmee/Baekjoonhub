import sys

n = int(sys.stdin.readline().strip())
val = 9999999999
stones = []
# stones_tu = []
dp = [0] + [val] * (n-1)

for i in range(n-1):
    s, b = map(int, sys.stdin.readline().strip().split())
    stones.append((s, b))
    # stones_tu.append((s, b))

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
            # print("0: " + str(stones[j][0] == stones_tu[j][0]))
            dp1 = min(dp1, energy + stones[j][0])
        if i + 2 <= n:
            # print("1: " + str(stones[j][1] == stones_tu[j][1]))
            dp2 = min(dp2, energy + stones[j][1])
        energy, dp1, dp2 = dp1, dp2, val
    min_energy = min(min_energy, energy)

print(min_energy)
