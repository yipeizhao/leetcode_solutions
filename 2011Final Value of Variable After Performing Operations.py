def Solutiono(operations):
    res= 0
    for item in operations:
        if item == '++X' or item =='X++':
            res +=1
        else:
            res-=1
    return res