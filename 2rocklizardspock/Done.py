# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name=='rock':
        number=0
    elif name=='Spock':
        number=1        
    elif name=='paper':
        number=2
    elif name=='lizard':
        number=3
    elif name=='scissors':
        number=4
    return number
def number_to_name(number):
    name=''
    if number==0:
        name='rock'
    elif number==1:
        name='Spock'
    elif number==2:
        name='paper'        
    elif number==3:
        name='lizard'
    elif number==4:
        name='scissors'
    return name
def rpsls(player_choice): 
    

    # print a blank line to separate consecutive games
    print "Player chooses ",player_choice
    # print out the message for the player's choice
    
    player_number=name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    
    comp_number=random.randrange(0,4)
    # compute random guess for comp_number using random.randrange()
    
    comp_choice=number_to_name(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    
    print "Computer chooses ",comp_choice
    # print out the message for computer's choice

    flag=player_number-comp_number
    
    if flag<0:
        flag+=5
    if flag==1 or flag==2:
        print "Player wins!"
    elif flag==3 or flag==4:
        print "Computer wins!"
    else:
        print "We have a Tie!"

    print "\n"
    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

