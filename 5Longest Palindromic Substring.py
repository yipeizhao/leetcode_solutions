def Solution(s):
    if len(s) == 1:
        return s
    res = ""
    for i in range(len(s)):
        for j in range(len(s)-1,0,-1):
            string = s[i:j+1]
            if string == string[::-1] and len(string)>len(res):
                res = string
            if j<i:
                break
    return res
s = "babadada"
print(Solution(s))