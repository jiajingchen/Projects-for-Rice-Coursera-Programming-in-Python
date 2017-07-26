# template for "Stopwatch: The Game"
import simplegui
# define global variables
global time,x,y
time=0
x=0
y=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d=t%10
    abc=(t-d)/10
    bc=abc%60
    c=bc%10
    b=(bc-c)/10
    a=(abc-bc)/60
    string=str(a)+":"+str(b)+str(c)+"."+str(d)
    return string

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start_handler():
    global time
    timer.start()
def button_stop_handler():
    global time,x,y
    if timer.is_running():
        y=y+1
        if format(time)[-1]=="0":
            x=x+1
    timer.stop()    
def button_reset_handler():
    global time,x,y
    time=0
    x=0
    y=0
    timer.stop()
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time=time+1


# define draw handler
def draw_handler(canvas):
    global time
    canvas.draw_text(format(time), [100, 100], 50, 'White')
    canvas.draw_text(str(x)+"/"+str(y), [320,40], 50, 'Green') 

# create frame
frame = simplegui.create_frame('Stop Watch', 400, 200)


# register event handlers
button1 = frame.add_button('Start', button_start_handler)
button1 = frame.add_button('Stop', button_stop_handler)
button1 = frame.add_button('Reset', button_reset_handler)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
# start frame
frame.start()
