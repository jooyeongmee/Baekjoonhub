class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int days = 0;
        String[] day = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
        for (int i = 1; i < a; i++) {
            if (i == 2) {
                days += 29;
            } else if (i <= 7) {
                days += (i % 2 == 0) ? 30 : 31;
            } else {
                days += (i % 2 == 0) ? 31 : 30;
            }
        }
        days += b;
        
        answer = (days % 7 == 0) ? "THU" : day[days % 7 - 1];
        
        
        
        return answer;
    }
}