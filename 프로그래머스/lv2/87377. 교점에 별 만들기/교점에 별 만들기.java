import java.util.*;

class Solution {
    private static class Point{
        public final long x, y;

        private Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }
    
    private Point intersection(long a, long b, long e, long c, long d, long f) {
        double underNum = a*d - b*c;
        if (underNum == 0) return null;
        double x = (b*f - e*d) / underNum;
        double y = (e*c - a*f) / underNum;
        return (x % 1 == 0 && y % 1 == 0) ? new Point((long)x, (long)y) : null;
    }
    
    private Point getMinimumLength(List<Point> points) {
        long minX = Long.MAX_VALUE;
        long minY = Long.MAX_VALUE;
        
        for (Point p: points) {
            if (p.x < minX) minX = p.x;
            if (p.y < minY) minY = p.y;
        }
        
        return new Point(minX, minY);
    }
    
    private Point getMaximumLength(List<Point> points) {
        long maxX = Long.MIN_VALUE;
        long maxY = Long.MIN_VALUE;
        
        for (Point p: points) {
            if (p.x > maxX) maxX = p.x;
            if (p.y > maxY) maxY = p.y;
        }
        
        return new Point(maxX, maxY);
    }
    
    public String[] solution(int[][] line) {
        
        List<Point> points = new ArrayList<>();
        for (int i = 0; i < line.length; i++) {
            for (int j = i+1; j < line.length; j++) {
                Point p = intersection(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);
                if (p != null) {
                    points.add(p);
                }
                
            }
        }
      
        Point minLength = getMinimumLength(points);
        Point maxLength = getMaximumLength(points);
        
        int w = (int) (maxLength.x - minLength.x + 1);
        int h = (int) (maxLength.y - minLength.y + 1);
        
        char[][] arr = new char[h][w];
        for (char[] row : arr) {
            Arrays.fill(row, '.');
        }
        
        for (Point p : points) {
            int x = (int) (p.x - minLength.x);
            int y = (int) (maxLength.y - p.y);
            arr[y][x] = '*';
        }
        
        String[] answer = new String[h];
        for (int i = 0; i < h; i++) {
            answer[i] = new String(arr[i]);
        }
        
        
        return answer;
    }
}