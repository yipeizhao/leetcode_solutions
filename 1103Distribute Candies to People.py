def Solution(candies,num_people):
    res = [0]*num_people
    n = 1
    while candies>=n:
        res[n%num_people-1] += n
        candies -= n
        n+=1
    res[n%num_people-1]+=candies
    return res
candies = 10
num_people = 3
print(Solution(candies, num_people))