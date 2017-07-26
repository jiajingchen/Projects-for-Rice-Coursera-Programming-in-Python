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
    for dummy_i in range(len(line)-len(sortlist)):
        sortlist.append(0)
   
    newlist=list(sortlist) # pairs of tiles are replaced with a tile of twice the value and a zero tile
    for dummy_i in range(len(sortlist)-1):     
        if sortlist[dummy_i]==sortlist[dummy_i+1]:
            sortlist[dummy_i+1]=0
            newlist[dummy_i]=2*sortlist[dummy_i]
            newlist[dummy_i+1]=0
         
    finallist=[]    # non-zero tiles slid over, with 0s at the end of the list  
    for tile in newlist:     
        if tile:
            finallist.append(tile)
    for dummy_i in range(len(newlist)-len(finallist)):
        finallist.append(0)
    return finallist
