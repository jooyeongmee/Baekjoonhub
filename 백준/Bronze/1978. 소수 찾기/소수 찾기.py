n = int(input())
data = list(map(int, input().split()))

def is_prime(n):
    if n == 1:
         return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(n):
    if is_prime(data[i]):
        count += 1
        
print(count)
    