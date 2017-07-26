"""
Clone of 2048 game.
"""

import poc_2048_gui
import math
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
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

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # initiate the variables
        self.height=grid_height
        self.width=grid_width
        self.grid=[]
        INITI_TILES={}# create a list of the indices for the initial tiles in each direction
        
        INITI_TILES[UP]= [(0, index) for index in range(self.width)]
        INITI_TILES[DOWN]= [(self.height-1, index) for index in range(self.width)]
        INITI_TILES[LEFT]= [(index,0) for index in range(self.height)]
        INITI_TILES[RIGHT]= [(index, self.width-1) for index in range(self.height)]
        
        self.reset() #call the reset function
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        #create a grid of height¡Áwidth zeros

        for dummy_i in range(0,self.height):
            self.grid.append(self.width*[0])

        self.new_tile()
        
        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        girdstring=""
        
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        move_flag=0 #a flag to determine if any tile has moved
        for item in INITI_TILES[direction]:
            temporary_list=[]
            indice_list=[]
            RANGE=int(math.fabs(OFFSETS[direction][0])*self.height+math.fabs(OFFSETS[direction][1])*self.width)
            for num in range(RANGE):
                indice_list.append((item[0]+num*OFFSETS[direction][0],item[1]+num*OFFSETS[direction][1]))
                temporary_list.append(self.grid[indice_list[num][0]][indice_list[num][1]])
            
            merge_list=merge(temporary_list)
             
            for num in range(RANGE):
                if self.grid[indice_list[num][0]][indice_list[num][1]]!=merge_list[num]:
                    move_flag+=1
            self.grid[indice_list[num][0]][indice_list[num][1]]=merge_list[num]

       
        if move_flag>0: # if any tile moved,add a new tile
            self.new_tile()

        

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        emptylist=[] #a list of all the empty square's indices
            for dummy_row in range(0,self.height):
                for dummy_col in range(0,self.width):
                    if get_tile(dummy_row,dummy_col)==0:
                        emptylist.append((dummy_row,dummy_col))
        random_num=random.randrange(0, 10) #a random num to determine 90%,10%
        if random_num==9:
            random_indice=random.choice(emptylist)
            set_tile(random_indice[0],random_indice[1],4)
        else:
            random_indice=random.choice(emptylist)
            set_tile(random_indice[0],random_indice[1],2)
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col]=value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
