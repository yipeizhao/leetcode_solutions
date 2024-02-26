def Solution(s):
    s=s.lower()
    vowels = ['a','e','i','o','u']
    res_a = 0;res_b=0
    for i in range(0,int(len(s)/2),1):
        if s[i] in vowels:
            res_a+=1
    for i in range(int(len(s)/2),len(s)):
        if s[i] in vowels:
            res_b+=1
    return res_a==res_b
s = "book"
print(Solution(s))