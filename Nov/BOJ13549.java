package Nov;

import java.io.*;
import java.util.*;

public class BOJ13549{
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());


        int[] dp = new int[100001];
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        Arrays.fill(dp, INF);
        dp[n] = 0;
        pq.offer(new int[]{0, n});

        while(!pq.isEmpty()){
            int[] top = pq.poll();
            int dist = top[0];
            int cur = top[1];

            if(cur == k) {
                System.out.println(dist);
                break;
            }
            if(dp[cur] < dist) continue;

            if(cur*2 <= 100000) {
                if (dp[cur] < dp[cur*2]) {
                    dp[cur*2] = dp[cur];
                    pq.offer(new int[]{dist, cur * 2});
                }
            }
            if(cur != 0) {
                if (dp[cur]+1 < dp[cur-1]) {
                    dp[cur-1] = dp[cur]+1;
                    pq.offer(new int[]{dist+1, cur-1});
                }
            }
            if(cur != 100000) {
                if(dp[cur]+1 < dp[cur+1]) {
                    dp[cur+1] = dp[cur]+1;
                    pq.offer(new int[]{dist+1, cur+1});
                }
            }
        }
    }
}
