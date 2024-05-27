def solution(score):
    rank = list(reversed(sorted(score)))
    for i in range(len(score)):
        score[i]=rank.index(score[i])
        if score[i]==0:
            score[i] = 'Gold Medal'
        elif score[i]==1:
            score[i] = 'Silver Medal'
        elif score[i] ==2:
            score[i] = 'Bronze Medal'
        else:
            score[i]+=1
            score[i]=str(score[i])
    return score
score = [10,3,8,9,4]
print(solution(score))