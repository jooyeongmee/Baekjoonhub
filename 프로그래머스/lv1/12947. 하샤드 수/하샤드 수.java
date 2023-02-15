class Solution {
    public boolean solution(int x) {
     
        int input = x;
        int sum = 0;
        for (int i = 0; input > 0; i++) {
            sum += input % 10;
            input /= 10;
        }
        
        return (x % sum == 0) ? true : false;
    }
}