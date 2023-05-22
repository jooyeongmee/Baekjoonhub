import sys

num = int(input())

files = {}
for i in range(num):
    name, ext = sys.stdin.readline().rstrip().split('.')
    if ext in files.keys():
        files[ext] += 1
    else:
        files[ext] = 1

for _ in sorted(files.keys()):
    print(_, files[_])