def solution(nums):
    nums = list(set(nums))
    if len(nums)<3:
        return max(nums)
    nums = sorted(nums)
    return nums[-3]

nums = [2,2,3,1]
print(solution(nums))