# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

# helper function to start and restart the game
def new_game():

    # initialize global variables used in your code here
    global  secret_number
    secret_number=random.randrange(0,100)

    print secret_number
    # remove this when you add your code    



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 

    new_game()


    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     

    new_game()
   
    
    
def input_guess(guess):
    # main game logic goes here	
    print "Guess was ", guess

    if int(guess)<secret_number:
        print "Higher"
    if int(guess)>secret_number:
        print "Lower"       
    if int(guess)==secret_number:
        print "Correct"
        new_game()    
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)
frame.add_button("Range: 0 - 1000", range1000)
frame.add_button("Range: 0 - 100", range100)

inp = frame.add_input('input a number', input_guess, 50)
# register event handlers for control elements and start frame


# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
