import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = new int[arr.length];
        int i = 0;
        for (int num : arr) {
            if (num % divisor == 0) {
                answer[i] = num;
                i++;
            }
        }
        
        
        if (i == 0) {
            answer[i] = -1;
            i++;
        }
        answer = Arrays.copyOfRange(answer, 0, i);
        Arrays.sort(answer);
        
        
        return answer;
    }
}