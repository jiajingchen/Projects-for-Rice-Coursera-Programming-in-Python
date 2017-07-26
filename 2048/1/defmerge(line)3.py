"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    sortlist=[] # non-zero tiles slid over, with 0s at the end of the list
    for tile in line:     
        if tile:
            sortlist.append(tile)
    for j in range(len(line)-len(sortlist)):
        sortlist.append(0)
    # pairs of tiles are replaced with a tile of twice the value and a zero tile
    newlist=list(sortlist)
    for i in range(len(sortlist)-1):     
        if sortlist[i]==sortlist[i+1]:
            sortlist[i+1]=0
            newlist[i]=2*sortlist[i]
            newlist[i+1]=0
    # non-zero tiles slid over, with 0s at the end of the list       
    finallist=[]    
    for tile in newlist:     
        if tile:
            finallist.append(tile)
    for j in range(len(newlist)-len(finallist)):
        finallist.append(0)
    return finallist
