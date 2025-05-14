data = []
for i in range(9):
    data.append(int(input()))
    
data.sort()
result = [0] * 7

def comb(depth, start):
    if depth == 7:
        if sum(result) == 100:
            for i in range(7):
                print(result[i])
            exit()
        return
    for i in range(start, 9):
        result[depth] = data[i]
        comb(depth+1, i+1)
    
    
comb(0, 0)
