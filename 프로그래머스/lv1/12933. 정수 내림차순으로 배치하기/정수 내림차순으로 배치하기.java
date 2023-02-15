import java.util.*;
class Solution {
    public long solution(long n) {
        long answer = 0;
        String[] input = ("" + n).split("");
        Arrays.sort(input, Collections.reverseOrder());
        answer = Long.parseLong(String.join("", input));
        return answer;
    }
}