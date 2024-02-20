def Solution(nums):
    res = []
    number = ''
    for i in range(len(nums)):
        number += str(nums[i])
        if int(number,2)%5==0:
            res.append(True)
        else:
            res.append(False)
    return res

nums = [0,1,1]
print(Solution(nums))