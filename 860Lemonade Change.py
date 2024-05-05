def solution(bills):
    change = {5:0,10:0}
    for item in bills:
        if item == 5:
            change[item]+=1
        elif item == 10:
            change[item]+=1
            change[5]-=1
        elif item == 20:
            if change[10]>=1 and change[5]>=1:
                change[10]-=1
                change[5]-=1
            elif change[5]>=3:
                change[5]-=3
            else:
                return False
        if change[5]<0 or change[10]<0:
            return False
    return True

bills = [5,5,5,10,20]
print(solution(bills))