import sys

n, m, r = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

num = min(n, m) // 2
for _ in range(r):
    for t in range(num):
        temp = arr[t][t]

        # 위끝: <-
        for i in range(t, m-t-1):
            arr[t][i] = arr[t][i+1]
        # 오른쪽끝: ^|
        for i in range(t, n-t-1):
            arr[i][m-t-1] = arr[i+1][m-t-1]
        # 아래끝: ->
        for i in range(m-t-1, t, -1):
            arr[n-t-1][i] = arr[n-t-1][i-1]
        # 왼쪽끝: |v
        for i in range(n-t-1, t, -1):
            arr[i][t] = arr[i-1][t]

        arr[t+1][t] = temp

for r in arr:
    for c in r:
        print(c, end=" ")
    print()


# 4 4 2
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# 5 4 3 2