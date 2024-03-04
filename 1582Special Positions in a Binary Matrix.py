def Solution(mat):
    transpose = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    res = 0
    for row in mat:
        for j in range(len(row)):
            if row[j] ==1:
                if sum(row)==1 and sum(transpose[j])==1:
                    res+=1
                else:
                    continue
    return res
mat = [[1,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]
print(Solution(mat))