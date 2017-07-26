# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PAD_VOL = 10
#initiate the paddle and ball pos
paddle1_pos=[0,HEIGHT/2-HALF_PAD_HEIGHT]
paddle2_pos=[WIDTH,HEIGHT/2-HALF_PAD_HEIGHT]
paddle1_vel, paddle2_vel =0,0
ball_pos = [WIDTH/2,HEIGHT/2]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1 , 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    
    #update paddles pos
    paddle1_pos[1]+= paddle1_vel
    paddle2_pos[1]+= paddle2_vel
    # draw paddles
    canvas.draw_line((paddle1_pos[0], paddle1_pos[1]), (paddle1_pos[0],paddle1_pos[1]+PAD_HEIGHT ), PAD_WIDTH, 'White')
    canvas.draw_line((paddle2_pos[0], paddle2_pos[1]), (paddle2_pos[0],paddle2_pos[1]+PAD_HEIGHT ), PAD_WIDTH, 'White')

   
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = PAD_VOL
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -PAD_VOL
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = PAD_VOL
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = -PAD_VOL       
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['down']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle2_vel = 0        
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
