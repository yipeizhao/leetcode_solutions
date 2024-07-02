def solution(nums):
    res = 0
    for i in nums:
        if i%3!=0:
            res+=1
    return res

print(solution([1,2,3,4]))