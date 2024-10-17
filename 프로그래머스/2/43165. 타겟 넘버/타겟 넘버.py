count = 0
def dfs(i, total, numbers, target):
    global count
    if i == len(numbers)-1:
        if total == target:
            count += 1
        return
    
    dfs(i+1, total+numbers[i+1], numbers, target)
    dfs(i+1, total-numbers[i+1], numbers, target)
        
    
            
        
        

def solution(numbers, target):
    global count
    dfs(0, numbers[0], numbers, target)
    dfs(0, -numbers[0], numbers, target)
        
    return count