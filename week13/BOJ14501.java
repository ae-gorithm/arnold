package week13;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ14501 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n = Integer.parseInt(br.readLine());
		int[] dp = new int[n+1];

		for(int i = 0; i < n; i++){
			st = new StringTokenizer(br.readLine());
			int index = Integer.parseInt(st.nextToken());
			int money = Integer.parseInt(st.nextToken());
			if (i != 0){
				dp[i] = Math.max(dp[i], dp[i-1]);
			}
			if(i+index <= n){
				dp[i+index] = Math.max(money + dp[i], dp[i+index]);
			}
		}
		Arrays.sort(dp);
		System.out.println(dp[n]);
	}
}
