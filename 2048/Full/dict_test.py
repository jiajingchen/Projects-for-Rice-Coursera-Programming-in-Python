import random
height=4
width=5

grid=[]
emptylist=[]
for dummy_i in range(0,height):
    grid.append(width*[0])
    emptylist.append(width*[0])
    
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

INITI_TILES={}
# create a list of the indices for the initial tiles in each direction
INITI_TILES[UP]= [(0, index) for index in range(width)]
INITI_TILES[DOWN]= [(height-1, index) for index in range(width)]
INITI_TILES[LEFT]= [(index,0) for index in range(height)]
INITI_TILES[RIGHT]= [(index, width-1) for index in range(height)]


#random 2

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
    

print random_num
print emptylist
print random_indice

print grid
            
