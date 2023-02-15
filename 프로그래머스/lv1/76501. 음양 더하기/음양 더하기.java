class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int i = 0;
        while (i < absolutes.length) {
            answer += absolutes[i] * ((signs[i] == true) ? 1 : -1);
            i++;
        }
        return answer;
    }
}