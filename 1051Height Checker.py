def Solution(heights):
    res = 0
    expected = sorted(heights)
    for i in range(len(expected)):
        if expected[i]!=heights[i]:
            res+=1
    return res
heights = [5,1,2,3,4]
print(Solution(heights))