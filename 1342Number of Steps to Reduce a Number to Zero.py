def Solution(num):
    c = 0
    while num!= 0:
        if num%2 == 0:
            num = num/2
            c+=1
        else:
            num-=1
            c+=1
    return c

num =14
print(Solution(num))