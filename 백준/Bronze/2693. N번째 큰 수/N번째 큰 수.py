t = int(input())

for i in range(t):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    print(data[2])