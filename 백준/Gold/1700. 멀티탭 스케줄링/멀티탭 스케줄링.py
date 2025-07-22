n, k = map(int, input().split())
input_data = list(map(int, input().split()))

multi = []
count = 0
for i in range(k):
    if not input_data[i] in multi:
        if len(multi) < n:
            multi.append(input_data[i])
        else:
            last_index = -1
            target = -1
            for j in range(len(multi)):
                if not multi[j] in input_data[i:]:
                    target = j
                    break
                target_index = input_data.index(multi[j], i+1)
                if target_index > last_index:
                    last_index = target_index
                    target = j

            multi[target] = input_data[i]
            count += 1
               
print(count)
        