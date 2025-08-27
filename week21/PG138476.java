package week21;

import java.util.*;

class PG138476 {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int max = Arrays.stream(tangerine).max().getAsInt();
        Integer[] counter = new Integer[max+1];
        Arrays.fill(counter, 0);
        for (int v : tangerine) {
            counter[v]++;
        }
        Arrays.sort(counter, Collections.reverseOrder());
        for (int v : counter) {
            k -= v;
            answer += 1;
            if (k <= 0) {
                // System.out.println(Arrays.toString(counter));
                return answer;
            }
        }
        return -1;
    }
}
