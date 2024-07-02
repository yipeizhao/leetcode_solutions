def solution(s):
    s = s.replace(' ','')
    s = ''.join(ch for ch in s if ch.isalnum())
    s = s.lower()
    for i in range(int(len(s)/2)):
        if s[i] != s[-i-1]:
            print(i)
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(solution(s))