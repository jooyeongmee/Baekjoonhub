class Solution {
    public int solution(int num) {
        long input = (long) num;
        int answer = 0;
        while (true) {
            if (input == 1) return answer;
            if (answer >= 500) return -1;
            
            answer++;
            
            if (input % 2 == 0) {
                input /= 2;
                
            } else {
                input = input * 3 + 1;
            }
          
        }
      
    }
}