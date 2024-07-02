def solution(n,roads):
    connections = {}
    res = 0
    for i in range(n):
        connections[i]=0
    for item in roads:
        connections[item[0]]+=1
        connections[item[1]]+=1
    
    importance = sorted(connections.items(), key=lambda kv: 
                 (kv[1], kv[0]))
    importance = dict(zip([item[0] for item in importance],range(1,n+1)))
    for item in roads:
        res+=importance[item[0]]+importance[item[1]]

    return res

n = 5
roads = [[0,3],[2,4],[1,3]]

print(solution(n,roads))