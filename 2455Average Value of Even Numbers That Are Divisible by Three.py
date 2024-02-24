def Solution(nums):
    c=0
    res=0
    for item in nums:
        if item%6 == 0:
            c+=1
            res+=item
    return int(res/c) if c!=0 else 0