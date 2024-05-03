def solution(n):
    if n<2:
        return n
    res = [0,1,1]
    for i in range(3,n+1):
        next_val = res[0]+res[1]+res[2]
        res[0],res[1],res[2] = res[1],res[2],next_val
    return res[2]

n = 4
print(solution(n))