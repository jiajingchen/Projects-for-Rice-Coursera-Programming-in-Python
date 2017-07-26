# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
global remain_guess

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "\nNew game. Range is from 0 to 100"
    global remain_guess
    remain_guess=7
    print "Number of remaining guesses is",remain_guess
    global secret_number

    secret_number=random.randint(0,100)
    print secret_number
    # remove this when you add your code    



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "New game. Range is from 0 to 100"   
    remain_guess=7
    print "Number of remaining guesses is",remain_guess
    global secret_number
    secret_number=random.randint(0,100)
    print secret_number
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "New game. Range is from 0 to 1000" 
    global remain_guess
    remain_guess=10
    print "Number of remaining guesses is",remain_guess

    global secret_number
    secret_number=random.randint(0,1000)
    print secret_number

    
def input_guess(guess):
    # main game logic goes here	
    print "Guess was",guess
    global remain_guess
    remain_guess-=1
    print "Number of remaining guesses is",remain_guess
    if remain_guess>0:
        if int(guess)<secret_number:
            print "Higher"
        if int(guess)>secret_number:
            print "Lower"       
        if int(guess)==secret_number:
            print "Correct"
            new_game()
    if remain_guess<=0:
        print "You ran out of guesses.  The number was",secret_number
        new_game()
        
    print "\n"
# create frame
frame = simplegui.create_frame('The Guess Game', 300, 300)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)
inp = frame.add_input('My label', input_guess, 50)

# call new_game 
new_game()
