n, s = map(int, input().split())
input_data = list(map(int, input().split()))

if sum(input_data) < s:
    print(0)
    exit()
    
length = n + 1
start = 0
end = 0
current_sum = 0
while start < n:
    if current_sum >= s:
        length = min(length, end - start)
        current_sum -= input_data[start]
        start += 1
    elif end == n:
        break
    else:
        current_sum += input_data[end]
        end += 1
    

print(length if length != n + 1 else 0)