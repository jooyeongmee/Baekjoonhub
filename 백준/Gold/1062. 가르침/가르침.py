from itertools import combinations

n, k = map(int, input().split())

if k < 5: 
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()
 
data = []
for _ in range(n):
    input_str = input().strip()
    data.append(input_str)

max_count = 0
alphabet = ['a', 'n', 't', 'i', 'c']

combi_list = combinations("bdefhgjklmopqrsuvwxyz", k-5)

for combi in combi_list:
    for i in combi:
        alphabet.append(i)
    
    count = 0
    for word in data:
        if all(char in alphabet for char in word):
            count += 1
    if count > max_count:
        max_count = count
    alphabet = ['a', 'n', 't', 'i', 'c']

print(max_count)
