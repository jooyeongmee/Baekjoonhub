import sys

num = int(sys.stdin.readline().strip())
status = [0] + list(map(int, sys.stdin.readline().split()))
student = int(sys.stdin.readline().strip())
li = []
for i in range(student):
    gender, switch_num = map(int, sys.stdin.readline().split())
    li.append((gender, switch_num))

for (g, s) in li:
    if g == 1:
        for i in range(s, num+1):
            if i % s == 0:
                status[i] = status[i] ^ 1

    elif g == 2:
        i = s-1
        j = s+1
        while True:
            if i == 0 or j == num+1:
                for k in range(i+1, j):
                    status[k] = status[k] ^ 1
                break
            if status[i] != status[j]:
                for k in range(i+1, j):
                    status[k] = status[k] ^ 1
                break
            i -= 1
            j += 1

count = 0
for i in range(num+1):
    if count >= 20:
        print()
        count = 0
    if i != 0:
        count += 1
        print(status[i], end=" ")

