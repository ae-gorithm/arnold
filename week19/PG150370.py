def changeDate(y, m, d):
    return d + (m * 28) + (y * 12 * 28)

def solution(today, terms, privacies):
    answer = []
    ty, tm, td = map(int, today.split("."))
    todayDate = changeDate(ty, tm, td)
    newTerms = [0 for _ in range(26)]

    for t in terms:
        kind, period = t.split()
        newTerms[ord(kind)-65] = int(period) * 28
    
    for i in range(len(privacies)):
        info = privacies[i]
        date, kind = info.split()
        y, m, d = map(int, date.split("."))
        changedDate = changeDate(y, m, d) + newTerms[ord(kind)-65]

        if changedDate <= todayDate:
            answer.append(i+1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))