# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number

    secret_number=random.randint(0,100)
    print secret_number
    # remove this when you add your code    



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number=random.randint(0,100)
    print secret_number
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number=random.randint(0,1000)
    print secret_number

    
def input_guess(guess):
    # main game logic goes here	
   

    if int(guess)<secret_number:
        print "Higher"
    if int(guess)>secret_number:
        print "Lower"       
    if int(guess)==secret_number:
        print "Correct"
    
# create frame
frame = simplegui.create_frame('The Guess Game', 300, 300)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)
inp = frame.add_input('My label', input_guess, 50)

# call new_game 
new_game()# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
