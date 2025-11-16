package Nov;

import java.util.*;
import java.io.*;

public class BOJ15666{
    public static int n;
    public static int m;
    public static Integer[] arr;
    public static int[] sel;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int l = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        Integer[] tmp = new Integer[l];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<l; i++) tmp[i] = Integer.parseInt(st.nextToken());
        Set<Integer> set = new HashSet<>(Arrays.asList(tmp));
        n = set.size();
        arr = set.toArray(new Integer[n]);
        Arrays.sort(arr);
        sel = new int[m];

        comb(0, 0);
    }

    public static void comb(int start, int depth){
        if (depth == m){
            String ret = Arrays.toString(sel).replaceAll("[\\[\\],]", "");
            System.out.println(ret);
            return;
        }

        for(int i=start; i<n; i++){
            sel[depth] = arr[i];
            comb(i, depth+1);
        }
    }
}
