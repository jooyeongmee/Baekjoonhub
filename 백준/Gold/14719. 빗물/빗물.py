h, w = map(int, input().split())
data = list(map(int, input().split()))

new_data = []
left = 0
right = -1
for i in range(1, w):
    # print(i, left, right)
    if data[i] >= data[left] or data[i] > data[right]:
        new_data.append(data[left:(i+1)])
        left = i

if left < w-1:
    new_data.append(data[left::])

# print(new_data)

def concat_data(data_list, stop):
    if data_list == []:
        return []
    temp = [data_list[0].copy()]
    for i in range(1, len(data_list)):
        if data_list[i][0] <= data_list[i][-1] and temp[-1][0] >= temp[-1][-1]:
            temp[-1] = temp[-1] + data_list[i][1::]
            stop = False
        else:
            temp.append(data_list[i])
    
    if not stop:
        return concat_data(temp.copy(), True)
    return temp

final_data = concat_data(new_data, False)
# print(final_data)

count = 0
for data_range in final_data:
    min_height = min(data_range[0], data_range[-1])
    if min_height == 0:
        continue
    for i in range(len(data_range)):
        if data_range[i] < min_height:
            count += min_height - data_range[i]

print(count)