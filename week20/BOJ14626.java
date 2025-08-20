package week20;

import java.io.*;
import java.util.*;

public class BOJ14626 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        String isbn = br.readLine();
        int checkSum = 0;
        int loc = -1;
        int ans = -1;
        Integer[] arr = {10, 3, 6, 9, 2, 5, 8, 1, 4, 7};

        for (int i = 0; i < isbn.length(); i++){
            if (isbn.charAt(i) == '*') {
                loc = i;
                continue;
            }
            if (i % 2 == 0){
                checkSum += Character.getNumericValue(isbn.charAt(i));
            } else{
                checkSum += Character.getNumericValue(isbn.charAt(i)) * 3;
            }
        }

        if (loc % 2 == 0) {
            ans = 10 - checkSum % 10;
        } else {
            ans = List.of(arr).indexOf(10 - checkSum%10);
        }
        System.out.println(ans%10);
    }
}

// 3 6 9 2 5 8 1 4 7