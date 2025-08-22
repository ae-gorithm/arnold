package week21;

import java.util.*;

class PG43164 {
    public String[] solution(String[][] tickets) {
        String[] answer;
        Map<String, PriorityQueue<String>> map = new HashMap<>();


        for (String[] ticket : tickets) {
            if (!map.containsKey(ticket[0])) {
                PriorityQueue<String> list = new PriorityQueue<>();
                list.offer(ticket[1]);
                map.put(ticket[0], list);
            } else {
                map.get(ticket[0]).offer(ticket[1]);
            }
        }

        List<String> path = new ArrayList<>();
        Stack<String> stack = new Stack<>();
        stack.push("ICN");

        while (!stack.empty()) {
            String nextCity = stack.peek();

            if (map.get(nextCity) == null || map.get(nextCity).isEmpty()) {
                path.add(stack.pop());
            } else {
                stack.push(map.get(nextCity).poll());
            }
        }

        answer = new String[path.size()];
        for (int i=0; i<path.size(); i++){
            answer[i] = path.get(path.size()-i-1);
        }
        return answer;
    }
}