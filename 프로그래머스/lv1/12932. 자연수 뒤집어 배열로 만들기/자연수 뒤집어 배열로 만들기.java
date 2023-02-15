import java.util.*;
class Solution {
    public int[] solution(long n) {
        String temp = "";
        int count = 0;
        for (int i = 0; n > 0; i++) {
            count++;
            temp += n % 10;
            n /= 10;
        }
    
        int[] answer = new int[count];
        for (int i = 0; i < count; i++) {
            answer[i] = temp.charAt(i) - '0';
        }
        return answer;
    }
}