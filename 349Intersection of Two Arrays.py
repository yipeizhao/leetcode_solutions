def solution(nums1,nums2):
    return set(nums1).intersection(set(nums2))

nums1 = [1,2,2,1]; nums2 = [2,2]
print(solution(nums1, nums2))