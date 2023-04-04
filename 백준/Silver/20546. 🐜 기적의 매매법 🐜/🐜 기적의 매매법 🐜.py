import sys

money = int(sys.stdin.readline().strip())
stocks = list(map(int, sys.stdin.readline().split()))

#준현
bnp = money
bnp_num = 0
i = 0
while i < 14:
    if bnp == 0:
        break
    if stocks[i] <= bnp:
        bnp_num += bnp // stocks[i]
        bnp = bnp % stocks[i]
    i += 1

#성민
timing = money
timing_num = 0
up = 0
down = 0
for j in range(14):
    if j != 0 and stocks[j-1] < stocks[j]:
        up += 1
        down = 0
    if j != 0 and stocks[j-1] > stocks[j]:
        down += 1
        up = 0
    if down >= 3:
        if stocks[j] <= timing:
            timing_num += timing // stocks[j]
            timing = timing % stocks[j]
    elif up >= 3:
        timing += stocks[j] * timing_num
        timing_num = 0

#결과계산
bnp_result = bnp + bnp_num * stocks[-1]
timing_result = timing + timing_num * stocks[-1]

if bnp_result > timing_result:
    print("BNP")
elif bnp_result < timing_result:
    print("TIMING")
else:
    print("SAMESAME")


