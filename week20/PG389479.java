package week20;

import java.util.*;

class PG389479 {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int[] numOfServer = new int[24];
        Arrays.fill(numOfServer, 1);
        for (int i = 0; i < 24; i++) {
            if (players[i] >= numOfServer[i] * m) {
                int server = (players[i] - numOfServer[i] * m) / m + 1;
                answer += server;
                for (int j = i; j < i + k; j++) {
                    if (j > 23) {
                        break;
                    }
                    numOfServer[j] += server;
                }
            }
            System.out.println(Arrays.toString(numOfServer));
        }
        return answer;
    }
}
