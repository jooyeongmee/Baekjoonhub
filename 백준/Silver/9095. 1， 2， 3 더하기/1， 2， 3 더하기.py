import sys

t = int(sys.stdin.readline())

num_list = [-1]
for _ in range(t):
    num = int(sys.stdin.readline())
    num_list.append(num)

    dp = [-1, 1, 2, 4] + [0] * (num-3)
    for i in range(4, num+1):
        for j in range(1, 4):
            dp[i] += dp[i-j]

    print(dp[num])