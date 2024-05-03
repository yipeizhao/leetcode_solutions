def solution(nums):
    return (sorted(nums)[-1]-1)*(sorted(nums)[-2]-1)

nums = [1,5,4,5]
print(solution(nums))