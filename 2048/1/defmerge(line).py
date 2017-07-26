"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    #all of the non-zero tiles slid over to the beginning of the list
    #with the appropriate number of zeroes at the end of the list
    sortlist=[]
    for i in range(len(line)):     
        if line[i]!=0:
            sortlist.append(line[i])
    for j in range(len(line)-len(sortlist)):
        sortlist.append(0)
        
    #  pairs of tiles in the first list are replaced
    #with a tile of twice the value and a zero tile
    newlist=[]
    for tile in sortlist:
        newlist.append(tile)
    for i in range(len(sortlist)-1):     
        if sortlist[i]==sortlist[i+1]:
            sortlist[i+1]=0
            newlist[i]=2*sortlist[i]
            newlist[i+1]=0
    #
    finallist=[]
    for i in range(len(newlist)):     
        if newlist[i]!=0:
            finallist.append(newlist[i])
    for j in range(len(newlist)-len(finallist)):
        finallist.append(0)


    return finallist


print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2,2])
print merge([8, 16, 16, 8]) 
