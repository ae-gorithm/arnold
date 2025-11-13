package Nov;

import java.util.*;
import java.io.*;

public class BOJ1504{
    static final int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<int[]>> edges = new ArrayList<>();
        for(int i=0;i<n+1;i++) {
            edges.add(new ArrayList<>());
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            edges.get(a).add(new int[]{b, c});
            edges.get(b).add(new int[]{a, c});
        }

        st = new StringTokenizer(br.readLine());
        int v1 = Integer.parseInt(st.nextToken());
        int v2 = Integer.parseInt(st.nextToken());

        long path1 = -1, path2 = -1;

        long dist1_v1 = dijk(1, v1, n, edges);
        long dist_v1_v2 = dijk(v1, v2, n, edges);
        long dist_v2_n = dijk(v2, n, n, edges);

        if (dist1_v1 != INF && dist_v1_v2 != INF && dist_v2_n != INF) {
            path1 = dist1_v1 + dist_v1_v2 + dist_v2_n;
        }

        long dist1_v2 = dijk(1, v2, n, edges);
        long dist_v1_n = dijk(v1, n, n, edges);

        if (dist1_v2 != INF && dist_v1_v2 != INF && dist_v1_n != INF) {
            path2 = dist1_v2 + dist_v1_v2 + dist_v1_n;
        }

        long answer = -1;
        if (path1 != -1 && path2 != -1) {
            answer = Math.min(path1, path2);
        } else if (path1 != -1) {
            answer = path1;
        } else {
            answer = path2;
        }

        System.out.println(answer);
    }

    public static int dijk(int start, int end, int n, ArrayList<ArrayList<int[]>> edges){
        int[] dp = new int[n+1];

        for(int i=0;i<n+1;i++) {
            Arrays.fill(dp, INF);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[0] - o2[0];
            }
        });

        pq.offer(new int[]{0, start});
        dp[start] = 0;

        while(!pq.isEmpty()){
            int[] top = pq.poll();
            int dist = top[0];
            int cur = top[1];

            if(dp[cur] < dist) continue;
            for(int[] next : edges.get(cur)){
                int nextNode = next[0];
                int nextDist = next[1];

                if(dp[nextNode] > dp[cur] + nextDist){
                    dp[nextNode] = dp[cur] + nextDist;
                    pq.offer(new int[]{dp[cur] + nextDist, nextNode});
                }
            }
        }
        return dp[end];
    }
}
