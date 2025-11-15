package Nov;

import java.util.*;
import java.io.*;

public class BOJ7579{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] mem = new int[n+1];
        int[] cost = new int[n+1];

        st = new StringTokenizer(br.readLine());
        for(int i=1; i<n+1; i++){
            mem[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i=1; i<n+1; i++){
            cost[i] = Integer.parseInt(st.nextToken());
        }
        int sum = 0;
        for(int i=0; i<n+1; i++) sum += cost[i];

        int[][] dp = new int[n+1][sum+1];
        for(int i=0; i<n+1; i++){
            Arrays.fill(dp[i], 0);
        }

        for(int i=1; i<n+1; i++){
            for(int j=0; j<sum+1; j++){
                if (j >= cost[i]) dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-cost[i]] + mem[i]);
                else dp[i][j] = dp[i-1][j];
            }
        }

        int ans = 0;
        for(int i=0; i<sum+1; i++){
            if (dp[n][i] >= m) {
                ans = i;
                break;
            }
        }
        System.out.println(ans);
    }
}
