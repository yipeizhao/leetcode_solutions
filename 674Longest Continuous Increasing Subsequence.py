def Solution(nums):
    res = 0
    for i in range(len(nums)-1):
        temp =1
        for j in range(i+1,len(nums)):
            if nums[j]<=nums[j-1]:
                i=j
                break
            else:
                temp+=1
        res = max(res,temp)
    return res
nums = [2,2,2,2,2]
print(Solution(nums))