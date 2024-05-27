def solution(nums):
    nums = sorted(nums)
    x = 0
    for i in range(len(nums)):
        while x<nums[i]:
            x+=1
            if len(nums)-i==x:
                return x
    return -1
    
nums = [0,4,3,0,4]
print(solution(nums))