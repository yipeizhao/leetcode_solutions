def solution(nums1,nums2):
    i = 0; j =0
    while True:
        if nums1[i]==nums2[j]:
            return nums1[i]
        elif nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
        if i >= len(nums1) or j >=len(nums2):
            break
    return -1

nums1 = [1,2,4]; nums2 = [3]
print(solution(nums1,nums2))