m = int(input())
n = int(input())

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

sum = 0
minVal = 10000
for i in range(m, n+1):
    if is_prime(i):
        sum += i
        if i < minVal:
            minVal = i
            
if sum == 0:
    print(-1)
else:
    print(sum)
    print(minVal)