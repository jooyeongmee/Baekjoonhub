a, b = map(int, input().split())

def gcd(a, b):
    min_val = min(a, b)
    for i in range(min_val, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def lcm(a, b):
    max_val = max(a, b)
    min_val = min(a, b)
    i = 1
    while True:
        if (max_val * i) % min_val == 0:
            return max_val * i
        i+=1    
        
print(gcd(a, b))
print(lcm(a, b))