import random
height=4
width=5

grid=[]
emptylist=[]
for dummy_i in range(0,height):
    grid.append(width*[0])
    emptylist.append(width*[0])
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
    
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
RANGEDICT={UP: (1, 0),
           DOWN: (1, 0),
           LEFT: (0, 1),
           RIGHT: (0, 1)}

INITI_TILES={}
# create a list of the indices for the initial tiles in each direction
INITI_TILES[UP]= [(0, index) for index in range(width)]
INITI_TILES[DOWN]= [(height-1, index) for index in range(width)]
INITI_TILES[LEFT]= [(index,0) for index in range(height)]
INITI_TILES[RIGHT]= [(index, width-1) for index in range(height)]


#random 2
strr='''
emptylist=[]
for dummy_row in range(0,height):
    for dummy_col in range(0,width):
        if grid[dummy_row][dummy_col]==0:
            emptylist.append((dummy_row,dummy_col))
random_num=random.randrange(0, 10)
if random_num==9:
    random_indice=random.choice(emptylist)
    grid[random_indice[0]][random_indice[1]]=4
else:
    random_indice=random.choice(emptylist)
    grid[random_indice[0]][random_indice[1]]=2
'''    
grid[0][0]=2
grid[1][1]=2
grid[2][2]=2
grid[3][3]=2
print grid


# def move:
import math
direction=UP
move_flag=0
for item in INITI_TILES[direction]:
    temporary_list=[]
    indice_list=[]
    
    RANGE=int(math.fabs(OFFSETS[direction][0])*height+math.fabs(OFFSETS[direction][1])*width)
    for num in range(RANGE):
        indice_list.append((item[0]+num*OFFSETS[direction][0],item[1]+num*OFFSETS[direction][1]))
        temporary_list.append(grid[indice_list[num][0]][indice_list[num][1]])
    merge_list=merge(temporary_list)
    for num in range(RANGE):
        if grid[indice_list[num][0]][indice_list[num][1]]!=merge_list[num]:
            move_flag+=1
        grid[indice_list[num][0]][indice_list[num][1]]=merge_list[num]
'''    print indice_list
    print temporary_list
    print merge_list
    print move_flag
print grid
print move_flag
'''

girdstringlist=[]
for item in grid:
    girdstringlist.append(item)
    output_str=str(girdstringlist)
    output_str.replace(",",''[:2])
print output_str







    


            
