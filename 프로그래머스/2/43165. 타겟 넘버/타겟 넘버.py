count = 0
def dfs(i, total, numbers, target):
    global count
    if i == len(numbers):
        if total == target:
            count += 1
        return
    
    dfs(i+1, total+numbers[i], numbers, target)
    dfs(i+1, total-numbers[i], numbers, target)
        
    
            
        
        

def solution(numbers, target):
    global count
    dfs(0, 0, numbers, target)
        
    return count