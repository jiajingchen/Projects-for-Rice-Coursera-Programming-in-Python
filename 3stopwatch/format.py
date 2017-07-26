

def format(t):
    d=t%10
    abc=(t-d)/10
    bc=abc%60
    c=bc%10
    b=(bc-c)/10
    a=(abc-bc)/60
    string=str(a)+":"+str(b)+str(c)+"."+str(d)
    print string

format(0)
format(11)
format(613)
format(321)
