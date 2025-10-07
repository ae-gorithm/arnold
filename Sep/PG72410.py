def solution(new_id):
    answer = case7(case6(case5(case4(case3(case2(case1(new_id)))))))
    return answer

def case1(new_id):
    return new_id.lower()

def case2(new_id):
    s = ""
    for ch in new_id:
        if ch == '-' or ch == '_' or ch == '.':
            s += ch
        elif 97 <= ord(ch) <= 122 or 48 <= ord(ch) <= 57:
            s += ch
    return s

def case3(new_id):
    s = ""
    for i in range(len(new_id)-1):
        if new_id[i] !='.':
            s += new_id[i]
        elif new_id[i] == '.' and new_id[i+1] != '.':
            s += '.'
    s += new_id[-1]
    return s

def case4(new_id):
    return new_id.strip(".")

def case5(new_id):
    if new_id == "":
        return "a"
    return new_id

def case6(new_id):
    return case4(new_id[:15])

def case7(new_id):
    if len(new_id) <= 2:
        w = new_id[-1] * (3-len(new_id))
        return new_id + w
    return new_id
