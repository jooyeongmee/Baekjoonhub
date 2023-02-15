class Solution {
    public long solution(int price, int money, int count) {
        long pay = 0;
        for (int i = 1; i <= count; i++) {
            pay += price * i;
        }

        if (pay > money) return pay - money;
        else return 0;
            
        
    
    }
}