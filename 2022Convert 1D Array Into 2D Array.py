def Solution(original,m,n):
    if m*n!=len(original):
        return []
    res = [[]]
    column = 0
    for i in range(len(original)):
        if column==n:
            res.append([])
            column=0
        res[-1].append(original[i])
        column+=1
    return res
        
original = [1,1,1,1]
m = 4
n = 1
print(Solution(original, m, n))