import java.util.*;
class Solution {
    public String solution(String s) {
        
        String answer = "";
        String[] arr = s.split(" ", -1);
        
        for (String str : arr) {
      
            char[] char_list= str.toCharArray();
            for (int i = 0; i < char_list.length; i++) {
                if (i % 2 == 0) {
                    char_list[i] = Character.toUpperCase(char_list[i]);
                } else {
                    char_list[i] = Character.toLowerCase(char_list[i]);
                }
            }

            answer += String.valueOf(char_list) + " ";

            
        }
        
        return answer.substring(0, answer.length() - 1);
        
    }
}