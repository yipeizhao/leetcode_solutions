def Solution(nums1,nums2,m,n):
    for _ in range(len(nums1)-m):
        nums1.pop()
    for item in nums2:
        nums1.append(item)
    nums1.sort()
    print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Solution(nums1, nums2, m, n)