def Solution(nums1,nums2):
    nums = sorted(nums1+nums2)
    l = len(nums)
    return (nums[int(l/2)]+nums[(int(l/2))-1])/2 if l%2 == 0 else nums[int(l/2)]

nums1 = [2]
nums2 = []
print(Solution(nums1,nums2))