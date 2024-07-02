def solution(nums1,nums2):
    res = []
    counts = [nums1.count(item) for item in nums1]
    counts = dict(zip(nums1,counts))
    for item in nums2:
        if item in counts.keys():
            if counts[item] >0:
                res.append(item)
                counts[item]-=1
    return res
nums1 = [1,2,2,1]
nums2 = [2]
print(solution(nums1,nums2))