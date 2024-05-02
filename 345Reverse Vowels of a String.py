def Solution(s):
    s = list(s)
    v = ['a','e','i','o','u','A','E','I','O','U']
    forward = 0
    backward = len(s)-1
    f_flag = False
    b_flag = False
    while forward<=backward:
        if s[forward] not in v:
            forward+=1
        else:
            f_flag = True
        if s[backward] not in v:
            backward-=1
        else:
            b_flag = True
        if f_flag&b_flag:
            s[forward],s[backward] = s[backward],s[forward]
            f_flag = False
            b_flag = False
            forward+=1;backward-=1
    return ''.join(s)

s = 'aA'
print(Solution(s))