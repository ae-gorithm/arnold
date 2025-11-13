package Nov;

import java.io.*;
import java.util.*;

public class BOJ1238{
    static final int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<int[]>> edges = new ArrayList<>();
        int[][] dp = new int[n+1][n+1];
        for (int i=0; i<=n; i++) {
            edges.add(new ArrayList<>());
            Arrays.fill(dp[i], INF);
        }

        for(int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            edges.get(a).add(new int[]{b, c});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[0]-o2[0];
            }
        });

        int[] res = new int[n+1];

        for (int i=1; i<=n; i++){
            dp[i][i] = 0;
            pq.offer(new int[]{0, i});

            while(!pq.isEmpty()){
                int[] top = pq.poll();
                int dist = top[0];
                int cur = top[1];

                if (dp[i][cur] < dist) continue;
                for (int[] next : edges.get(cur)) {
                    int nextNode = next[0];
                    int nextDist = next[1];

                    if(dp[i][nextNode] > dp[i][cur]+nextDist) {
                        dp[i][nextNode] = dp[i][cur]+nextDist;
                        pq.offer(new int[]{dp[i][cur]+nextDist, nextNode});
                    }
                }
            }
            res[i] = dp[i][x];
        }

        for(int i=1; i<=n; i++){
            res[i] += dp[x][i];
        }
        Arrays.sort(res);
        System.out.println(res[n]);
    }
}