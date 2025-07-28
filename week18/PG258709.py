from itertools import combinations, product
from bisect import bisect_left, bisect_right
import heapq
def solution(dice):
    n = len(dice)
    diceNo = [i for i in range(1, n+1)]

    comb = list(combinations(dice, n//2))
    noComb = list(combinations(diceNo, n//2))
    l = len(comb)
    res = []
    for i in range(l//2):
        win = 0
        draw = 0
        lose = 0
        diceComb = list(map(sum, product(*comb[i])))
        diceComb2 = sorted(list(map(sum, product(*comb[-i-1]))))
        
        for num in diceComb:
            leftIdx = bisect_left(diceComb2, num)
            rightIdx = bisect_right(diceComb2, num)
            win += leftIdx
            draw += rightIdx - leftIdx
            lose += len(diceComb) - rightIdx

        heapq.heappush(res, [-win, noComb[i]])
        heapq.heappush(res, [-lose, noComb[-i-1]])
    return list(heapq.heappop(res)[1])
    

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

print(solution(dice))

"""
a b c / a b d / a b e / a b f / a c d / a c e / a c f / a d e / a d f / a e f 
b c d / b c e / b c f / b d e / b d f / b e f / c d e / c d f / c e f / d e f
"""