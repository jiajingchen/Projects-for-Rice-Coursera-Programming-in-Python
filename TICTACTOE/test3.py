import random
SCORE_CURRENT=1
SCORE_OTHER=1
B1=[[0 for i in range(3)]for j in range(3)]
scores=[[0 for i in range(3)]for j in range(3)]
B1[1][1]="X"
B1[2][2]="O"
B1[0][2]="O"

for row in B1:
    print row
B2=[[0 for i in range(3)]for j in range(3)]
B2[1][1]="X"
B2[2][2]="O"
B2[0][2]="O"

# player (PLAYERX or PLAYERO),


def who_wins(board):
    result=None
    for row in board:#row
        if row==["X","X","X"]:
            result= "PLAYERX"
        if row==["O","O","O"]:
            result= "PLAYERO"  
    for col in range(3):#col
        if board[0][col]==board[1][col]==board[2][col]=="X":
            result= "PLAYERX"
        if board[0][col]==board[1][col]==board[2][col]=="O":
            result= "PLAYERO" 
    if board[0][0]==board[1][1]==board[2][2]=="X":  #diagonal
        result= "PLAYERX"
    if board[2][0]==board[1][1]==board[0][2]=="X":
        result= "PLAYERX"
    if board[0][0]==board[1][1]==board[2][2]=="O":
        result= "PLAYERO"
    if board[2][0]==board[1][1]==board[0][2]=="O":
        result= "PLAYERO"
    if result!="O" and result!="X":
        flag=0 # a flag to determine empty suqare
        for row in board:
            for col in row:
                if col==0:
                    flag=1
        if flag!=1:
            result="DRAW"
        
    return result
    
print who_wins([[0,0,0],[0,"X",0],[0,"0","X"]])
    
def pick_random_move(board,player):
    mark=player[6]
    empty_list=[]
    for row in range(3):
        for col in range(3):
            if board[row][col]==0:
                empty_list.append((row,col))
    if empty_list!=[]: # if there is an empty space to make a move
        pick_random_move=random.choice(empty_list)
        board[pick_random_move[0]][pick_random_move[1]]=mark




def swtich_player(player):
    if player=="PLAYERX":
        return "PLAYERO"
    if player=="PLAYERO":
        return "PLAYERX"
    
def mc_trial(board, player):
    
#This function takes a current board and the next player to move.  
#play a game starting with the given player by making random moves, alternating between players.   
#return when the game is over
# the function should modify the board input.
    while who_wins(board)==None:
        pick_random_move(board,player)
        if who_wins(board)==None:
            pick_random_move(board,swtich_player(player))
      #test
        for row in board:
            print row
        print who_wins(board)
      
    return board

def mc_update_scores(scores, board, player):
    # takes a grid of scores (a list of lists)  
#The function should score the completed board and update the scores grid. 
    #As the function updates the scores grid directly
    # it does not return anything
    current_scores=[[0 for i in range(3)]for j in range(3)]
    if who_wins(board)==player: # if wins
        for row in range(3):
            for col in  range(3): #score each squares
                if board[row][col]==0:
                    current_scores[row][col]=0
                if board[row][col]==player[6]:
                    current_scores[row][col]=SCORE_CURRENT
                if board[row][col]==swtich_player(player)[6]:
                    current_scores[row][col]=-SCORE_OTHER
    if who_wins(board)==swtich_player(player): # if wins
        for row in range(3):
            for col in  range(3): #score each squares
                if board[row][col]==0:
                    current_scores[row][col]=0
                if board[row][col]==player[6]:
                    current_scores[row][col]=-SCORE_CURRENT
                if board[row][col]==swtich_player(player)[6]:
                    current_scores[row][col]=SCORE_OTHER

    if who_wins(board)=="DRAW":
        for row in range(3):
            for col in  range(3): #score each squares
                current_scores[row][col]=0

    #add current score list to the sum of score list:
    for row in range(3):
        for col in  range(3):
             scores[row][col]+=current_scores[row][col]   






def get_best_move(board, scores):
    #find all of the empty squares with the maximum score
    # and randomly return one of them as a (row, column) tuple. 
    empty_list=[]
    for row in range(3):
        for col in range(3):
            if board[row][col]==0:
                empty_list.append((row,col))
    max_score=0
    max_indice=[]
    for square_indice in empty_list:
        if scores[square_indice[0]][square_indice[1]]>= max_score:
            max_score=scores[square_indice[0]][square_indice[1]]
            max_indice=[square_indice[0],square_indice[1]]
    return (max_indice[0],max_indice[1])

def mc_move(board, player, trials):
    #use the Monte Carlo simulation described above
    #to return a move for the machine player a (row, column) tuple
    # use the other functions you have written!
    
    current_board=[[0 for i in range(3)]for j in range(3)]
    for row in range(3): #copy a board
        for col in range(3):
            current_board[row][col]==board[row][col]
            
    for dummy_n in range(trials):
        moved_board=mc_trial(board, player)
        mc_update_scores(scores,moved_board, player)
                
    return get_best_move(current_board,scores)

print mc_move(B1,"PLAYERX",10)    
