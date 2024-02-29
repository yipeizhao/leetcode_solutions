def Solution(height):
    res = 0
    left = 0
    right = len(height)-1
    while left<right:
        res = max( min(height[left],height[right])*(right-left),res)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return res
height = [1,8,6,2,5,4,8,3,7]

print(Solution(height))