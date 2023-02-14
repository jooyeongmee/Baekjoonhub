class Solution {
    public int solution(String s) {
        int answer = 0;
        int count_target = 0;
        int not_target = 0;
        int i = 0;
       
        while (true) {

            if (i == s.length() -1) {
                answer++;
                break;
            }
            char target = s.charAt(0);
            // System.out.println(target);
            if (target == s.charAt(i)) {
                count_target++;
            } else {
                not_target++;
            }
            // System.out.printf("index: %d, c: %d, n: %d\n", i, count_target, not_target);
            if (count_target == not_target) {
                answer++;
                
                s = s.substring(i+1, s.length());
                count_target = 0;
                not_target = 0;
                i = 0;
                
                continue;

            } 
            if (count_target == s.length()) {
                answer++;
                break;
            }
            i++;
        }
        
        return answer;
    }
}