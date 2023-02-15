import java.util.*;
import java.lang.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        String num3 = "";
        for (int i = 0; n > 0; i++){
            num3 += n % 3;
            n /= 3;
        }

        for (int i = 0; i < num3.length(); i++) {
            answer += (num3.charAt(num3.length() - i - 1) - '0') * Math.pow(3, i);
        }
        
        return answer;
    }
}