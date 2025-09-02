package week22;

class PG12985 {
    public int solution(int n, int a, int b) {
        int answer = 1;
        int cmp = n/2;

        while (n != 2) {
            int t = isOtherSide(cmp, a, b);
            if (t == 0) {
                answer++;
            } else if (t == 1) {
                cmp = cmp + n/4;
            } else {
                cmp = cmp - n/4;
            }
            n /= 2;
        }
        return answer;
    }

    public int isOtherSide(int n, int a, int b) {
        if ((a <= n && b > n) || (a > n && b <= n)) {
            return 0;
        } else if (a > n && b > n) {
            return 1;
        }
        return -1;
    }
}
// 4 7
// 1 4 / 5 7
// 1 2 3 4 / 5 6 7 8



//         / 9 11 n = 4, cmp = 10
// 1 3 5 7 / 9 11 13 15 n = 8, cmp = 12 -> 6
// 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16  n = 16, cmp = 8 -> 12
