package week22;

import java.util.*;
import java.io.*;

class BOJ17352{
    static int[] parent;
    static int n;
    static StringBuilder sb = new StringBuilder();
    public static int find(int x) {
        if (parent[x] == x) return parent[x];

        parent[x] = find(parent[x]);
        return parent[x];
    }

    public static void union(int a, int b) {
        a = find(a);
        b = find(b);

        if (a > b) parent[a] = b;
        else parent[b] = a;
    }

    public static void print() {
        for (int i=1; i<n; i++) {
            for (int j=i+1; j<=n; j++) {
                if (find(parent[i]) != find(parent[j])) {
                    sb.append(i + " " + j);
                    System.out.println(sb);
                    return;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        parent = new int[n+1];

        for (int i=1; i<=n; i++) {
            parent[i] = i;
        }
        String str = "";
        while ((str = br.readLine()) != null) {
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (find(a) != find(b)) {
                union(a, b);
            }
        }

        print();
    }
}