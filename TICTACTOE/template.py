"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    
    
    
    # the function should modify the board input.
    pass

def mc_update_scores(scores, board, player):
    # takes a grid of scores (a list of lists) 
    
    #As the function updates the scores grid directly
    # it does not return anything
    
    

def get_best_move(board, scores):
    #find all of the empty squares with the maximum score
    # and randomly return one of them as a (row, column) tuple. 
    

def mc_move(board, player, trials):
    #use the Monte Carlo simulation described above
    #to return a move for the machine player a (row, column) tuple
    # use the other functions you have written!
    pass

    



# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)