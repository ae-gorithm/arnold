package week20;

public class PG389478 {
    public int solution(int n, int w, int num) {
        int answer = 0;
        int totalHeight = ((n-1)/w) + 1;
        int y = ((num-1)/w) + 1;
        int x = findX(y, w, num);
        int lastX = findX(totalHeight, w, n);

        if (totalHeight % 2 == 0) {
            x = w - x + 1;
            lastX = w - lastX + 1;
        }

        System.out.println(x);
        System.out.println(lastX);

        answer = totalHeight - y;

        if (x <= lastX) answer += 1;

        return answer;
    }

    public int findX(int y, int w, int num){
        if (y % 2 == 0) {
            return y * w - num + 1;
        } else {
            return w - (y * w - num);
        }
    }
}
