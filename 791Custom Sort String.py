def solution(order,s):
    s = list(s)
    order = list(order)
    res = ''
    for item in order:
        for i in range(len(s)):
            if s[i]==item:
                res+=item
                s[i]=''
    return res+''.join(s)

order = "cba"; s = "abcd"
print(solution(order, s))