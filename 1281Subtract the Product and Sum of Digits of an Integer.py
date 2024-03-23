def Solution(n):
    prod = 1
    summ = 0
    for item in [int(x) for _,x in enumerate(str(n))]:
        prod*=item
        summ+=item
    return prod - summ
n = 4421
print(Solution(n))