import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> set = new HashSet<Integer>(); 
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                set.add(numbers[i] + numbers[j]);
            }
        }
        Integer[] ans_set = set.toArray(new Integer[set.size()]);
        int[] answer = Arrays.stream(ans_set).mapToInt(i->i).toArray();
    
        Arrays.sort(answer);
        return answer;
    }
}