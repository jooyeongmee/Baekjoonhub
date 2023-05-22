import sys

num = int(input())

files = {}
file_list = []
for i in range(num):
    name, ext = sys.stdin.readline().rstrip().split('.')
    if ext in files.keys():
        files[ext] += 1
    else:
        files[ext] = 1
        file_list.append(ext)

file_list.sort()
for _ in file_list:
    print(_, files[_])