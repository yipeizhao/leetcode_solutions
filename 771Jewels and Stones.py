def Solution(jewels,stones):
    res =0
    for item in jewels:
        res+=stones.count(item)
    return res