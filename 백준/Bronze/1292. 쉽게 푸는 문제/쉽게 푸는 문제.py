a, b = map(int, input().split())

data = []
sum = 0
for i in range(1, 1001):
    for j in range(i):
        data.append(i)
    

for i in range(a, b+1):
    sum += data[i-1]

print(sum)