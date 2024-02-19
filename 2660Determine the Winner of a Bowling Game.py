def solution(player1,player2):
    p1,p2 = 0,0
    p1Double = 0
    p2Double = 0
    for i in range(len(player1)):
        if p1Double==0:
            p1+=player1[i]
        else:
            p1+=2*player1[i]
            p1Double-=1
            
        if p2Double==0:
            p2+=player2[i]
        else:
            p2+=2*player2[i]
            p2Double-=1
            
        if player1[i]==10:
            p1Double = 2
        if player2[i]==10:
            p2Double = 2
    if p1==p2:
        return 0
    elif p1>p2:
        return 1
    else:
        return 2

player1 = [5,6,1,10]
player2 = [5,1,10,5]
print(solution(player1,player2))