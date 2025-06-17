package week12;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

class BOJ11725 {
	static ArrayList[] edges;
	static boolean[] visited;
	static int[] tree;
	static void dfs(int parent){

		for (Object next : edges[parent]) {
			if (visited[(int)next]) {
				continue;
			}
			visited[(int)next] = true;
			tree[(int)next] = parent;
			dfs((int)next);
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n = Integer.parseInt(br.readLine());

		edges = new ArrayList[n+1];
		visited = new boolean[n+1];
		tree = new int[n+1];

		for (int i = 0; i < n+1; i++) {
			edges[i] = new ArrayList();
			visited[i] = false;
			tree[i] = -1;
		}

		for (int i = 0; i < n-1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			edges[a].add(b);
			edges[b].add(a);
		}

		dfs(1);

		for (int i = 2; i <= n; i++) {
			System.out.println(tree[i]);
		}
	}
}