class Solution {
    public int solution(String s) {
        int answer = 0;
        int sign = 1;
        if (s.charAt(0) == '-') {
            sign = -1;
            s = s.substring(1, s.length());
        } else if (s.charAt(0) == '+') {
            s = s.substring(1, s.length());
        }
        answer = sign * Integer.parseInt(s);
        
        return answer;
    }
}