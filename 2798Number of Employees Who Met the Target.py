def solution(hours,target):
    return sum([1 if i>=target else 0 for i in hours])
print(solution([0,1,2,3,4],2))