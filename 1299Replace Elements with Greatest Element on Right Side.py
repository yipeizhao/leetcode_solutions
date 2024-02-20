def Solution(arr):
    greatest_element = -1
    for i in range(len(arr)-1,-1,-1):
        if greatest_element<arr[i]:
            arr[i],greatest_element=greatest_element,arr[i]
        else:
            arr[i]=greatest_element
    return arr
            

arr = [17,18,5,4,6,1]
print(Solution(arr))