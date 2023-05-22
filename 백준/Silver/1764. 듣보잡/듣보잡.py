import sys

n, m = map(int, input().split())
dic = {}
result = []

for i in range(n):
    dic[sys.stdin.readline()] = ''
for i in range(m):
    name = sys.stdin.readline()
    if name in dic.keys():
        result.append(name)

result.sort()
print(len(result))
print(''.join(result))