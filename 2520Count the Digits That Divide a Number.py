def Solution(num):
    res = 0
    for item in str(num):
        if num%int(item) == 0:
            res+=1
    return res

print(Solution(1248))