def solution(n):
    n = bin(n)[2:]
    for i in range(len(list(n))-1):
        if n[i]==n[i+1]:
            return False
    return True

n = 7
print(solution(n))