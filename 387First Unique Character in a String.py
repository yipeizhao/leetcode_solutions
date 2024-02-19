def solution(s):
    res = 10**5+1
    s_set = set(s)
    for item in s_set:
        if s.count(item) ==1:
            res = min(res,s.find(item))
    return -1 if res == 10**5+1 else res

s = 'leetcode'
print(solution(s))