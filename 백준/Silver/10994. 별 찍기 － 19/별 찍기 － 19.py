def make_border(start, end):
    for i in range(start, end):
        for j in range(start, end):
            if j == start or j == end-1:
                result[i][j] = "*"
            elif i == start or i == end-1:
                result[i][j] = "*"
            else:
                result[i][j] = " "
    return result


def print_result():
    for r in result:
        for c in r:
            print(c, end="")
        print()


n = int(input())
row = 4*(n-1) + 1
result = [[""] * row for _ in range(row)]

i = 0
while i < row:
    make_border(i, row-i)
    i += 2

print_result()

