def solution(nums):
    res = []
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return [nums[i],int((1+len(nums))*len(nums)/2-sum(nums)+nums[i])]
    return res

nums = [1,2,2,4]
print(solution(nums))