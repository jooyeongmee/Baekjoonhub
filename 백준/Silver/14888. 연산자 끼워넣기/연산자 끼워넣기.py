n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

operator = []
for i in range(plus):
    operator.append("+")
for i in range(minus):
    operator.append("-")
for i in range(mul):
    operator.append("*")
for i in range(div):
    operator.append("//")

possible_operators = set()

def permutation(depth, temp_arr, visited):
    if depth == n-1:
        key = tuple(temp_arr)
        if key not in possible_operators:
            possible_operators.add(key)
        return
    for i in range(n-1):
        if not visited[i]:
            visited[i] = True
            temp_arr[depth] = operator[i]
            permutation(depth+1, temp_arr, visited)
            visited[i] = False
                  
permutation(0, [""] * (n-1), [False] * (n-1))
# print(possible_operators, len(possible_operators))

def calculate(operators):
    result = a[0]
    for i in range(n-1):
        if operators[i] == "+":
            result += a[i+1]
        elif operators[i] == "-":
            result -= a[i+1]
        elif operators[i] == "*":
            result *= a[i+1]
        else:
            if result < 0:
                result = -((-result) // a[i+1])
            else:   
                result //= a[i+1]
    return result

max_val = -9999999999
min_val = 9999999999
for ops in list(possible_operators):
    sum = calculate(ops)
    # print(sum, possible_operators[i])
    if sum > max_val:
        max_val = sum
    if sum < min_val:
        min_val = sum

print(max_val)
print(min_val)