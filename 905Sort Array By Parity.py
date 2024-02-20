def Solution(nums):
    res = []
    for item in nums:
        if item%2 == 0:
            res.insert(0,item)
        else:
            res.append(item)
    return res