package Nov;

import java.util.*;
import java.io.*;

public class BOJ11779{
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<int[]>> edges = new ArrayList<>();
        ArrayList<ArrayList<Integer>> path = new ArrayList<>();
        for(int i=0; i<n+1; i++){
            edges.add(new ArrayList<>());
            path.add(new ArrayList<>());
        }

        for(int i=0; i<m; i++){
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

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        int[] dp = new int[n+1];
        // String[] path = new String[n+1];


        Arrays.fill(dp, INF);

        dp[start] = 0;
        path.get(start).add(start);
        pq.offer(new int[]{0, start});

        while(!pq.isEmpty()){
            int[] top = pq.poll();
            int dist = top[0];
            int curr = top[1];

            if(dp[curr] < dist) continue;

            for(int[] next : edges.get(curr)){
                int nextNode = next[0];
                int nextDist = next[1] + dp[curr];

                if(dp[nextNode] > nextDist){
                    dp[nextNode] = nextDist;
                    //path[nextNode] = path[curr] + " " + nextNode;
                    ArrayList<Integer> tmp = (ArrayList<Integer>) path.get(curr).clone();
                    tmp.add(nextNode);
                    path.set(nextNode, tmp);
                    pq.offer(new int[]{nextDist, nextNode});
                }
            }
        }
        System.out.println(dp[end]);
        System.out.println((path.get(end)).size());
        System.out.println(path.get(end).toString().replaceAll("[\\[\\],]", ""));
    }
}