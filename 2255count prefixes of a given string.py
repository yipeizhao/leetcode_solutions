def solution(words,s):
    res = 0
    for item in words:
        if item == s[0:len(item)]:
            res+=1
    return res
words = ["a","b","c","ab","bc","abc"]
s = "abc"
print(solution(words, s))