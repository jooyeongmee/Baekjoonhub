import java.util.*;

class Solution {
    
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> ht = new HashMap<String, Integer>();
        
        for (String p : participant) {
            if (ht.containsKey(p)) {
                ht.put(p, ht.get(p) + 1);
            } else {
                ht.put(p, 1); 
            }  
        }
        
        for (String c : completion) {
            if (ht.get(c) > 1) {
                ht.put(c, ht.get(c) - 1);
            } else {
                ht.remove(c); 
            }  
        }
        
        for (String s : ht.keySet()) {
            answer = s;
            break;
        }
        
        return answer;
    }
}