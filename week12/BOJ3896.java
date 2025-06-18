package week12;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ3896 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		boolean[] prime = new boolean[1299710];
		int n = 1299710;
		int root = (int)Math.pow(n, 0.5);

		for (int i = 2; i < root; i++) {
			if (!prime[i]){
				for (int j = i+i; j < n; j+=i){
					prime[j] = true;
				}
			}

		}

		int T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			if (!prime[k]) {
				System.out.println(0);
			} else {
				int left = k;
				int right = k;

				while (true) {
					if (prime[left]) {
						left--;
					}
					if (prime[right]) {
						right++;
					}
					if (!prime[left] && !prime[right]) {
						System.out.println(right-left);
						break;
					}
				}
			}
		}
	}
}

/*
2 3
3 4 5
5 6 7
7 8 9 10 11
11 12 13
13 14 15 16 17
17 18 19
19 20 21 22 23
23 24 25 26 28 29
29 30 31
31 32 33 34 35 36 37
37 38 39 40 41
41 42 43
43 44 45 46 47

 */