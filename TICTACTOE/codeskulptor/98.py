"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 50         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
    
def pick_random_move(board,player): 
    '''
    if there is an empty space to make a move
    '''
    if board.get_empty_squares()!=[]:
        pick_random_move_indice=random.choice(board.get_empty_squares())
        board.move(pick_random_move_indice[0],pick_random_move_indice[1], player)


    
def mc_trial(board, player): 
    '''
    #This function takes a current board and the next player to move
    # play a game starting with the given player by making random moves, alternating between players.   
    #return when the game is over
    #the function should modify the board input.
    '''
    while board.check_win()==None:
        pick_random_move(board,player)
        if board.check_win()==None:
            pick_random_move(board,provided.switch_player(player))
    
    return board

def mc_update_scores(scores, board, player): 
    '''
    # takes a grid of scores (a list of lists)
    #The function should score the completed board and update the scores grid. 
    #As the function updates the scores grid directly
    # it does not return anything
    '''
    current_scores=[[0 for dummy_i in range(board.get_dim())]for dummy_j in range(board.get_dim())]
    if board.check_win()==player: # if wins
        for row in range(board.get_dim()):
            for col in  range(board.get_dim()): #score each squares
                if board.square(row,col)==0:
                    current_scores[row][col]=0
                if board.square(row,col)==player:
                    current_scores[row][col]=SCORE_CURRENT
                if board.square(row,col)==provided.switch_player(player):
                    current_scores[row][col]=-SCORE_OTHER
    if board.check_win()==provided.switch_player(player): # if wins
        for row in range(board.get_dim()):
            for col in  range(board.get_dim()): #score each squares
                if board.square(row,col)==0:
                    current_scores[row][col]=0  
                if board.square(row,col)==player:
                    current_scores[row][col]=-SCORE_CURRENT
                if board.square(row,col)==provided.switch_player(player):
                    current_scores[row][col]=SCORE_OTHER

    if board.check_win()=="DRAW":
        for row in range(board.get_dim()):
            for col in  range(board.get_dim()): #score each squares
                current_scores[row][col]=0

    #add current score list to the sum of score list:
    for row in range(board.get_dim()):
        for col in  range(board.get_dim()):
             scores[row][col]+=current_scores[row][col]   

def get_best_move(board, scores):  
    '''
    #find all of the empty squares with the maximum score
    # and randomly return one of them as a (row, column) tuple. 
    '''
    max_score=-100
    max_indice=[]
    for square_indice in board.get_empty_squares():
        if scores[square_indice[0]][square_indice[1]]>= max_score:
            max_score=scores[square_indice[0]][square_indice[1]]
            max_indice=[square_indice[0],square_indice[1]]
    if max_indice!=[]:
        return (max_indice[0],max_indice[1])

def mc_move(board, player, trials):
    '''
    #use the Monte Carlo simulation described above
    #to return a move for the machine player a (row, column) tuple
    # use the other functions you have written!
    '''
    scores=[[0 for dummy_i in range(board.get_dim())]for dummy_j in range(board.get_dim())]        
    for dummy_n in range(trials):
        moved_board=mc_trial(board.clone(), player)
        print moved_board
        
       
        mc_update_scores(scores,moved_board, player)
        print scores
    return get_best_move(board,scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
