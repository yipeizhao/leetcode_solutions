def solution(matches):
    res = [[],[]]
    winners = [item[0] for item in matches]
    losers = [item[1] for item in matches]
    wins = dict(zip(winners,[0]*len(winners)))
    for item in losers:
        wins[item]=0
    loss = dict(zip(losers,[0]*len(losers)))
    
    for item in winners:
        wins[item]+=1
    for item in losers:
        loss[item]+=1
        wins[item]-=10000
    for item in wins.keys():
        if wins[item] > 0:
            res[0].append(item)
    for item in loss.keys():
        if loss[item] == 1:
            res[1].append(item)
    return [sorted(res[0]),sorted(res[1])]

matches = [[2,3],[1,3],[5,4],[6,4]]
print(solution(matches))