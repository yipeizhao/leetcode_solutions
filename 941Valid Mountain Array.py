def solution(arr):
    flag = True
    if len(arr)<3:
        return False
    if arr[0]==max(arr) or arr[-1]==max(arr):
        return False
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            return False
        elif arr[i]>arr[i-1] and flag:
            pass
        elif arr[i]<arr[i-1]:
            if flag:
                flag = not flag
            else:
                pass
        else:
            return False
    return True

arr= [3,5,5]
print(solution(arr))