def Solution(n,m):
    res = 0
    for i in range(1,n+1):
        if i%m != 0:
            res+=i
        else:
            res-=i
    return res

n = 10
m=3
print(Solution(n,m))