package week22;

import java.util.*;

class PG87694 {
    static int n = 102;
    static int[][] board = new int[n][n];
    static boolean[][] visited = new boolean[n][n];
    static int[] dx = new int[] {1, 0, -1, 0};
    static int[] dy = new int[] {0, 1, 0, -1};

    public int solution(int[][] rectangle, int characterY, int characterX, int itemY, int itemX) {
        int answer = 0;
        Queue<int[]> q = new LinkedList<>();
        characterX *= 2;
        characterY *= 2;
        itemX *= 2;
        itemY *= 2;
        q.offer(new int[] {characterX, characterY});
        visited[characterX][characterY] = true;
        findLine(rectangle);

        while (q.size() != 0) {
            int l = q.size();

            for (int a=0; a<l; a++) {
                int[] tmp = q.poll();
                int x = tmp[0];
                int y = tmp[1];

                if (x == itemX && y == itemY) return answer/2;

                for (int i=0; i<4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx<0 || ny<0 || nx>=n || ny>=n || board[nx][ny] <= 0 || visited[nx][ny]) continue;
                    visited[nx][ny] = true;
                    q.offer(new int[] {nx, ny});
                }
            }
            answer++;
        }

        return -1;
    }

    public void findLine(int[][] rectangle) {
        for (int i=0; i<rectangle.length; i++) {
            for (int j=0; j<4; j++){
                rectangle[i][j] *= 2;
            }
        }
        for (int[] arr : rectangle) {
            int a1 = arr[0];
            int b1 = arr[1];
            int c1 = arr[2];
            int d1 = arr[3];
            int a2 = a1+1;
            int b2 = b1+1;
            int c2 = c1-1;
            int d2 = d1-1;

            board[b1][a1] += 1;
            board[d1+1][a1] -= 1;
            board[b1][c1+1] -= 1;
            board[d1+1][c1+1] += 1;

            board[b2][a2] -= 5;
            board[d2+1][a2] += 5;
            board[b2][c2+1] += 5;
            board[d2+1][c2+1] -= 5;
        }

        for (int i=0; i<n; i++) {
            for (int j=1; j<n; j++) {
                board[i][j] += board[i][j-1];
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=1; j<n; j++) {
                board[j][i] += board[j-1][i];
            }
        }
    }
}