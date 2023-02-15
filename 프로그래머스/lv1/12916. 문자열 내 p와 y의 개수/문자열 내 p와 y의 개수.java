class Solution {
    boolean solution(String s) {

        int count = 0;
        char[] input = s.toCharArray();
        for (char c : input) {
            if (Character.toLowerCase(c) == 'p') {
                count++;
            } else if (Character.toLowerCase(c) == 'y') {
                count--;
            }
        }


        return (count == 0) ? true : false;
    }
}