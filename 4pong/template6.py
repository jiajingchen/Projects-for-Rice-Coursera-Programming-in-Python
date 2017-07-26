# Implementation of classic arcade game Pong

import simplegui
import random
import math
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
PAD_VOL = 2
#initiate the paddle and ball pos
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel, paddle2_vel =0,0
ball_pos = [WIDTH/2,HEIGHT/2]
score1, score2 = 0 , 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    paddle1_pos=[0,HEIGHT/2-HALF_PAD_HEIGHT]
    paddle2_pos=[WIDTH,HEIGHT/2-HALF_PAD_HEIGHT]
    paddle1_vel, paddle2_vel =0,0
    ball_vel=[0,0]
    if direction == RIGHT:
        
        ball_vel[0]=random.randrange(2, 4)
        ball_vel[1]=-random.randrange(1, 3)
    if direction == LEFT:
        ball_vel[0]=-random.randrange(2, 4)
        ball_vel[1]=-random.randrange(1, 3)
                
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+= ball_vel[0]   
    ball_pos[1]+= ball_vel[1] 
    
    if ball_pos[1]<=BALL_RADIUS:
         ball_vel[1] = - ball_vel[1] 
    if ball_pos[1]>=HEIGHT-BALL_RADIUS: 
         ball_vel[1] = - ball_vel[1] 
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1 , 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen

    if paddle1_pos+paddle1_vel<=HEIGHT-HALF_PAD_HEIGHT and paddle1_pos+paddle1_vel>HALF_PAD_HEIGHT:
        paddle1_pos+= paddle1_vel
        
    if paddle2_pos+paddle1_vel<=HEIGHT-HALF_PAD_HEIGHT and paddle2_pos+paddle2_vel>HALF_PAD_HEIGHT:
        paddle2_pos+= paddle2_vel
        
        
    # draw paddles
    canvas.draw_line((0, paddle1_pos -PAD_HEIGHT), (0,paddle1_pos+PAD_HEIGHT ), PAD_WIDTH, 'White')
    canvas.draw_line((WIDTH, paddle2_pos -PAD_HEIGHT), (WIDTH,paddle2_pos+PAD_HEIGHT ), PAD_WIDTH, 'White')
  

    ball_touch1,ball_touch2=False,False
   
    # determine whether paddle and ball collide
    if abs(ball_pos[1] -  paddle1_pos) <  HALF_PAD_HEIGHT+BALL_RADIUS:
        ball_touch1=True
    if abs(ball_pos[1] -  paddle2_pos) <  HALF_PAD_HEIGHT+BALL_RADIUS:
        ball_touch2=True
        
    if ball_pos[0]<=  PAD_WIDTH +BALL_RADIUS and ball_touch1:
        ball_vel[0] = -ball_vel[0]
       
    if ball_pos[0]>= WIDTH - PAD_WIDTH - BALL_RADIUS and ball_touch2:
        ball_vel[0] = -ball_vel[0]
     
    
    if ball_pos[0]<  PAD_WIDTH +BALL_RADIUS:
        score2+=1
        spawn_ball(LEFT)
        
    if ball_pos[0]> WIDTH - PAD_WIDTH :
        score1+=1
        spawn_ball(RIGHT)
        
    # draw scores
    canvas.draw_text(str(score1), (20, 20), 12, 'Red')
    canvas.draw_text(str(score2), (400, 20), 12, 'Red')
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = PAD_VOL
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -PAD_VOL
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -PAD_VOL
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = PAD_VOL

        
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['down']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['w']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle2_vel = 0        
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
