import java.util.*;
import java.lang.*;
class Solution {
    public double solution(long n) {
        long answer = 0;
        double temp = Math.sqrt((double)n);
        if (temp % 1 != 0) {
            answer = -1;
        } else {
            answer = (long) Math.pow((temp + 1), 2);
        }
        return answer;
    }
}