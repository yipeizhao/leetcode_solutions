def solution(nums):
    if len(nums) <= 1:
        return -1
    nums = sorted(nums)
    j = len(nums)-1
    i = 0
    while i<=j:
        if nums[i]+nums[j] == 0:
            return nums[j]
        elif abs(nums[i])<nums[j]:
            j-=1
        else:
            i+=1
    return -1

nums = [-956,-831,-707]
print(solution(nums))