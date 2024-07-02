def solution(grid):
    res = 0
    grid_t = list(map(list, zip(*grid)))
    for i in range(len(grid)):
        for j in range(len(grid)):
            res+=min(max(grid[i]),max(grid_t[j]))-grid[i][j]
    return res

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(solution(grid))