input_data = list(input())
stack = []
for item in input_data:
    if item == "(" or item == "[" :
        stack.append(item)
    elif item == ")" :
        temp = 0
        while stack:
            parentheses = stack.pop()
            if isinstance(parentheses, int):
                temp += parentheses
            elif parentheses == "(":
                temp = temp * 2 if temp else 2
                stack.append(temp)
                break
            else:
                print(0)
                exit()
        if not stack:
            print(0)
            exit()
    elif item == "]" :
        temp = 0
        while stack:
            parentheses = stack.pop()
            if isinstance(parentheses, int):
                temp += parentheses
            elif parentheses == "[":
                temp = temp * 3 if temp else 3
                stack.append(temp)
                break
            else:
                print(0)
                exit()
        if not stack:
            print(0)
            exit()

result = 0
for item in stack:
    if not isinstance(item, int):
        print(0)
        exit()
    result += item
print(result)
            