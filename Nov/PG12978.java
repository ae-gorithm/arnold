package Nov;

import java.util.*;

public class PG12978 {
    static final int INF = Integer.MAX_VALUE;

    public int solution(int N, int[][] road, int K) {
        int answer = 0;

        ArrayList<ArrayList<int[]>> edges = new ArrayList<>();
        for(int i=0; i<N+1; i++){
            edges.add(new ArrayList<>());
        }
        for(int i=0; i<road.length; i++){
            edges.get(road[i][0]).add(new int[]{road[i][1], road[i][2]});
            edges.get(road[i][1]).add(new int[]{road[i][0], road[i][2]});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[1] - o2[1];
            }
        });

        int[] dp = new int[N+1];
        Arrays.fill(dp, INF);
        dp[1] = 0;

        pq.offer(new int[]{1, 0});

        while(!pq.isEmpty()){
            int[] top = pq.poll();
            int curr = top[0];
            int dist = top[1];

            if(dp[curr] < dist) continue;
            for(int[] next : edges.get(curr)){
                int nextNode = next[0];
                int nextDist = next[1] + dp[curr];

                if(dp[nextNode] > nextDist){
                    dp[nextNode] = nextDist;
                    pq.offer(new int[]{nextNode, nextDist});
                }
            }
        }
        for(int val : dp){
            if (val <= K){
                answer++;
            }
        }
        return answer;
    }
}
