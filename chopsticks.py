"""
By Harris Perdikoyiannis
"""

# Player 1
p1 = [1,1]
# Player 2
p2 = [1,1]

Player1Turn = True

Player1Win = 0
Player2Win = 0

def find(p1,p2,Player1Turn):
    if Player1Turn:
        if p1[0] < 5:
            if p2[0] < 5:
                # do move from l1 to l2
                p2Move1 = [p1[0]+p2[0], p2[1]] 
                find(p1,p2Move1,False)
            if p2[1] < 5:
                # do move from l1 to r2
                p2Move2 = [p2[0], p2[1]+p1[0]] 
                find(p1,p2Move2,False)

        if p1[1] < 5:
            if p2[0] < 5:
                # do move from r1 to l2
                p2Move1 = [p2[0]+p1[1], p2[1]] 
                find(p1,p2Move1,False)
            if p2[1] < 5:
                # do move from r1 to r2
                p2Move2 = [p2[0], p2[1]+p1[1]] 
                find(p1,p2Move2,False)
        
        if p1[0] >= 5 and p1[1] >= 5:
            # Player 1 lost
            global Player2Win
            Player2Win += 1

        # go to previous decision for player 2
        return
    else:
        if p2[0] < 5:
            if p1[0] < 5:
                # do move from l2 to l1
                p1Move1 = [p1[0]+p2[0], p1[1]] 
                find(p1Move1,p2,True)
            if p1[1] < 5:
                # do move from l2 to r1
                p1Move2 = [p1[0], p1[1]+p2[0]]
                find(p1Move2,p2,True)

        if p2[1] < 5:
            if p1[0] < 5:
                # do move from r2 to l1
                p1Move1 = [p1[0]+p2[1], p1[1]]
                find(p1Move1,p2,True)
            if p1[1] < 5:
                # do move from r2 to r1
                p1Move2 = [p1[0], p1[1]+p2[1]]
                find(p1Move2,p2,True)
        
        if p2[0] >= 5 and p2[1] >= 5:
            # Player 2 lost
            global Player1Win
            Player1Win += 1

        # go to previous decision for player 1
        return

find(p1,p2,Player1Turn)
print("# of winning outcomes for player 1: "+str(Player1Win))
print("# of winning outcomes for player 2: "+str(Player2Win))


