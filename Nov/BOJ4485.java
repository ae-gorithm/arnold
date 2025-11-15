package Nov;

import java.util.*;
import java.io.*;

public class BOJ4485{
    static int[] dx = new int[]{1, 0, -1, 0};
    static int[] dy = new int[]{0, 1, 0, -1};
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = 0;
        while(true){
            T++;
            st = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(st.nextToken());
            ArrayList<ArrayList<Integer>> board = new ArrayList<>();

            if(n == 0) break;

            for(int i=0; i<n; i++){
                st = new StringTokenizer(br.readLine());
                ArrayList<Integer> arr = new ArrayList<>();
                for(int j=0; j<n; j++){
                    arr.add(Integer.parseInt(st.nextToken()));
                }
                board.add(arr);
            }

            PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2){
                    return o1[2] - o2[2];
                }
            });
            int[][] dp = new int[n][n];
            for(int i=0; i<n; i++){
                Arrays.fill(dp[i], INF);
            }
            dp[0][0] = board.get(0).get(0);
            pq.offer(new int[]{0, 0, board.get(0).get(0)});
            while(!pq.isEmpty()){
                int[] top = pq.poll();
                int x = top[0];
                int y = top[1];
                int dist = top[2];

                if (dp[x][y] < dist) continue;

                for(int i=0; i<4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                    int ndist = dist + board.get(nx).get(ny);

                    if (ndist < dp[nx][ny]){
                        dp[nx][ny] = ndist;
                        pq.offer(new int[]{nx, ny, ndist});
                    }
                }
            }
            System.out.printf("Problem %d: %d", T, dp[n-1][n-1]);
            System.out.println();
        }
    }
}
