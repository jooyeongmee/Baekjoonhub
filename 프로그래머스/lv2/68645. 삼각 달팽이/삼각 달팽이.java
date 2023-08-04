import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[][] arr = new int[n][n];
        int length = n * (n + 1) / 2;
        int num = 1;
        int i = 0;
        int j = 0;
        while (num <= length) {
            //아래로 이동
            while (true) {
                
                if (i >= n || arr[i][j] > 0) {
                    i--;
                    break;
                }
                arr[i][j] = num;
                i++;
                num++;
                
            }
            j++;
            
            //오른쪽으로 이동
            while (true) {
                
                if (j >= n || arr[i][j] > 0) {
                    j--;
                    break;
                }
                arr[i][j] = num;
                j++;
                num++;
                
            }
            i--;
            j--;
            
            //대각선 위로 이동
            while (true) {
                
                if (i <= 0 || j <= 0 || arr[i][j] > 0) {
                    i++;
                    j++;
                    break;
                }
                arr[i][j] = num;
                i--;
                j--;
                num++;
                
            }
            i++;
        }
        
        int[] answer = new int[length];
        int idx = 0;
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < x+1; y++) {
                answer[idx] = arr[x][y];
                idx++;
            }
        }
        
        return answer;
    }
}