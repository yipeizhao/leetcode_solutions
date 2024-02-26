def Solution(nums):
    set_n = set(nums)
    for item in set_n:
        if nums.count(item) >= len(nums)/2:
            return item
nums = [3,2,3]
print(Solution(nums))