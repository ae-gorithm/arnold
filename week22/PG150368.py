def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    answer = []
    answers = []
    discount = [10, 20, 30, 40]
    dfs([], m, emoticons, users, answers)
    answers.sort(key = lambda x: [-x[0], -x[1]])
    return answers[0]


def dfs(comb, m, emoticons, users, answers):
    if len(comb) == m:
        tmp = [0, 0]
        for user_discount, money in users:
            total_value = 0
            for i in range(m):
                emoticon_discount = comb[i]
                value = emoticons[i]
                if user_discount <= emoticon_discount:
                    total_value += value * (1-(emoticon_discount/100))
            if total_value >= money:
                tmp[0] += 1
            else:
                tmp[1] += total_value
        answers.append(tmp)
        return
        
    for i in range(4):
        comb.append((i+1) * 10)
        dfs(comb, m, emoticons, users, answers)
        comb.pop()
        
# 이모티콘 - 할인율 조합

# [1, 1], [2, 1], [3,1]
# [1, 1], [2, 1], [3,2]
# [1, 1], [2, 1], [3,3]
# [1, 1], [2, 1], [3,4]

# [1, 1], [2,2], [3,1]
# [3,2]
# [3,3]
# [3,4]

# [1, 1], [2,3], [3,1]
# [3,2]
# [3,3]
# [3,4]

# [1, 1], [2,4], [3,1]
# [3,2]
# [3,3]
# [3,4]