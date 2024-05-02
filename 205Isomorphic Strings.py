def solution(s,t):
    if len(s)!=len(t):
        return False
    if s==t:
        return True
    d= {}
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]]=t[i]
        else:
            if d[s[i]]!=t[i]:
                return False
    s,t=t,s
    d= {}
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]]=t[i]
        else:
            if d[s[i]]!=t[i]:
                return False
    return True
s = "badc"; t = "baba"
print(solution(s,t))