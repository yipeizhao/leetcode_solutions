def Solution(arr):
    res = sum(arr)
    for i in range(3,len(arr)+1,2):
        for j in range(len(arr)-i+1):
            res+=sum(arr[j:j+i])
    return res
arr = [1,4,2,5,3]
print(Solution(arr))