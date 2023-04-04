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
        i = s - 1
        j = s + 1
        status[s] = status[s] ^ 1
        while i >= 1 and j <= num:
            if status[i] != status[j]:
                break
            status[i] = status[i] ^ 1
            status[j] = status[j] ^ 1
            i -= 1
            j += 1

for i in range(1, num+1):
    print(status[i], end=" ")
    if i % 20 == 0:
        print()




