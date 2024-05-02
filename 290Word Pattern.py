def solution(pattern,s):
    d = {}
    s = s.split(' ')
    if len(pattern)!= len(s):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in d.keys():
            if s[i] in d.values():
                return False
            d[pattern[i]] = s[i]
        if d[pattern[i]]!=s[i]:
            return False
    return True



pattern = "abba"; s = "dog cat cat dog"
print(solution(pattern,s))