package week21;

import java.util.*;

class PG42578 {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, List<String>> map = new HashMap<>();
        for (String[] arr : clothes) {
            if (!map.containsKey(arr[1])) {
                map.put(arr[1], new ArrayList<>());
            }
            map.get(arr[1]).add(arr[0]);
        }
        for (List<String> list : map.values()) {
            answer *= list.size()+1;
        }
        return answer-1;
    }
}
