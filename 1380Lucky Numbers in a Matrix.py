def Solution(matrix):
    res = []
    for item in matrix:
        col = item.index(min(item))
        cols = [rows[col] for rows in matrix]
        if item[col] == max(cols):
            res.append(item[col])
    return res

matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(Solution(matrix))