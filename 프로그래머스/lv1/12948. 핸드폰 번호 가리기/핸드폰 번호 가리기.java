class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int l = phone_number.length();
        String last = phone_number.substring(l-4, l);
        
        for (int i = 0; i < l-4; i++) {
            answer += "*";
        }
        answer += last;
        return answer;
    }
}