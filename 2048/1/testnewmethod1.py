
def merge(line):
    sortlist=[]
    for tile in line:     
        if tile!=0:
            sortlist.append(tile)
    for j in range(len(line)-len(sortlist)):
        sortlist.append(0)
    

    newlist=[]
    for tile in sortlist:
        newlist.append(tile)
    for i in range(len(sortlist)-1):     
        if sortlist[i]==sortlist[i+1]:
            sortlist[i+1]=0
            newlist[i]=2*sortlist[i]
            newlist[i+1]=0
    return newlist   

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2,2])
print merge([8, 16, 16, 8]) 
