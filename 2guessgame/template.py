# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    input_guess(inp.get_text())
    
    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    pass
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code
    print inp.get_text()

    
# create frame
frame = simplegui.create_frame('Testing', 100, 100)
frame.add_button("Range: 0 - 1000", range1000)
frame.add_button("Range: 0 - 100", range100)

inp = frame.add_input('My label', input_guess, 50)
# register event handlers for control elements and start frame
range100()
range1000()

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
