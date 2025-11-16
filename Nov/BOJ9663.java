package Nov;

import java.util.*;
import java.io.*;

public class BOJ9663{
    public static int[] arr;
    public static int n;
    public static int count = 0;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        arr = new int[n];

        back(0);
        System.out.println(count);
    }

    public static void back(int depth){
        if(depth == n){
            count++;
            return;
        }

        for(int i=0; i<n; i++){
            arr[depth] = i;

            if (possible(depth)) {
                back(depth+1);
            }
        }
    }

    public static boolean possible(int depth) {
        for(int j=0; j<depth; j++){
            if(arr[depth] == arr[j]) return false;
            if(Math.abs(j-depth) == Math.abs(arr[depth]-arr[j])) return false;
        }
        return true;
    }
}
