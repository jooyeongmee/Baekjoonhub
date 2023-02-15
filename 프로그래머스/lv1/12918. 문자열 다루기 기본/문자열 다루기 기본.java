class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        char[] input = s.toCharArray();
        if (input.length != 4 && input.length != 6) return false;
        for (char c : input) {
            if (Character.isLetter(c)) {
                answer = false;
                break;
            }
        }
        return answer;
    }
}