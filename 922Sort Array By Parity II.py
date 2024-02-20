def Solution(nums):
    last = []
    while last!=nums:
        last = nums.copy()
        odd = -1
        even = -1
        for i in range(len(nums)):
            if nums[i]%2 != i%2 and i%2 == 0:
                even = i
            elif nums[i]%2 != i%2 and i%2 == 1:
                odd = i
            if even != -1 and odd != -1:
                nums[odd],nums[even]=nums[even],nums[odd]
                even=-1;odd=-1
    return nums
    
nums = [648,831,560,986,192,424,997,829,897,843]
print(Solution(nums))