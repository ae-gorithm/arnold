package week13;

import java.io.*;
import java.util.*;

public class BOJ13904 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n = Integer.parseInt(br.readLine());


		PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[0] == o2[0]) {return o2[1] - o1[1];}
				return o2[0] - o1[0];
			}
		});

		int len = 0;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int dueDate = Integer.parseInt(st.nextToken());
			int score = Integer.parseInt(st.nextToken());

			len = Math.max(len, dueDate + score);
			pq.add(new int[] {score, dueDate});
		}
		int[] ans = new int[len+1];

		while (!pq.isEmpty()) {
			int[] cur = pq.poll();
			int score = cur[0];
			int dueDate = cur[1];
			for (int i = dueDate; i > 0; i--) {
				if (ans[i] == 0) {
					ans[i] = score;
					break;
				}
			}
		}

		System.out.println(Arrays.stream(ans).sum());
	}
}