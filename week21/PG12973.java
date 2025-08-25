package week21;

import java.util.*;

class PG12973 {
    public int solution(String s) {
        Stack<String> stack = new Stack<>();

        for (String ch : s.split("")) {
            if (stack.size() == 0) {
                stack.push(ch);
            } else {
                if (stack.peek().equals(ch)) {
                    stack.pop();
                } else {
                    stack.push(ch);
                }
            }
        }

        if (stack.size() == 0) {
            return 1;
        } else {
            return 0;
        }
    }
}
