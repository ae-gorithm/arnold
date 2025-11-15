package Nov;

import java.io.*;
import java.util.*;

public class BOJ3067{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for(int t = 0; t < T; t++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int[] coins = new int[n];

            st = new StringTokenizer(br.readLine());
            for(int i=0; i<n; i++){
                coins[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int[][] dp = new int[n+1][m+1];

            for(int i=1; i<=n; i++){
                dp[i][0] = 1;
            }

            for(int i=1; i<=n; i++){
                for(int j=1; j<=m; j++){
                    dp[i][j] = dp[i-1][j];
                    if(j >= coins[i-1]){
                        dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]];
                    }
                }
            }

            System.out.println(dp[n][m]);
        }
    }
}
