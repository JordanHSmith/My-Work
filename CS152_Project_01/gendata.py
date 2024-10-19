'''Jordan Smith
09/14/21
CS 152 B
Project 01'''

def ballistic1(t):
    p_i = 1
    v_i = 11
    a = -10
    p_f = p_i + (v_i*t) + (0.5*a*(t**2))
    return(p_f)

y = ballistic1(0.5)
print("f(0.5) is ",y)
y = ballistic1(1.0)
print("f(1.0) is ",y)

def ballistic2(p_i,v_i,a,t):
    p_f = p_i + (v_i*t) + (0.5*a*(t**2))
    return(p_f)
y = ballistic2(1,11,-10,0.5)
print("f(0.5) is ",y)
y = ballistic2(2,11,-10,0.5)
print("f(0.5) is ",y)

def computeAndOutput(p_i,v_i,a,t):
    y = ballistic2(p_i,v_i,a,t)
    fp = open( 'data.csv', 'a' )
    fp.write( str(t) + "," + str(y) + "\n" )
    fp.close()
    print(t,",",y)
computeAndOutput(2,11,-10,0.5)

def trajectory10(p_i,v,a,t_i):
    computeAndOutput(p_i,v,a,t_i)
    computeAndOutput(p_i,v,a,t_i + 0.1)
    computeAndOutput(p_i,v,a,t_i + 0.2)
    computeAndOutput(p_i,v,a,t_i + 0.3)
    computeAndOutput(p_i,v,a,t_i + 0.4)
    computeAndOutput(p_i,v,a,t_i + 0.5)
    computeAndOutput(p_i,v,a,t_i + 0.6)
    computeAndOutput(p_i,v,a,t_i + 0.7)
    computeAndOutput(p_i,v,a,t_i + 0.8)
    computeAndOutput(p_i,v,a,t_i + 0.9)
trajectory10(1,11,-10,0)
trajectory10(1,11,-10,1)

def trajectory100(p_i,v,a,t_i):
    trajectory10(p_i,v,a,t_i)
    trajectory10(p_i,v,a,t_i + 1)
    trajectory10(p_i,v,a,t_i + 2)
    trajectory10(p_i,v,a,t_i + 3)
    trajectory10(p_i,v,a,t_i + 4)
    trajectory10(p_i,v,a,t_i + 5)
    trajectory10(p_i,v,a,t_i + 6)
    trajectory10(p_i,v,a,t_i + 7)
    trajectory10(p_i,v,a,t_i + 8)
    trajectory10(p_i,v,a,t_i + 9)

trajectory100(1,1,15,30)
trajectory100(1,.45,15,30)
trajectory100(1,.213,15,30)

def clearFile():
    fp = open( 'data.csv', 'w' )
    fp.close()
clearFile()
