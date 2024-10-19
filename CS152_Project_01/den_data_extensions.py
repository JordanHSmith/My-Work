'''Jordan Smith
09/14/21
CS 152 B
Project 01'''

def ballistic1(t):
    pi = 1
    vi = 11
    a = -10
    pf = pi + (vi*t) + (0.5*a*(t**2))
    return(pf)

y = ballistic1(0.5)
print("f(0.5) is ",y)
y = ballistic1(1.0)
print("f(1.0) is ",y)

def ballistic2(pi,vi,a,t):
    pf = pi + (vi*t) + (0.5*a*(t**2))
    return(pf)
y = ballistic2(1,11,-10,0.5)
print("f(0.5) is ",y)
y = ballistic2(2,11,-10,0.5)
print("f(0.5) is ",y)

def computeAndOutput(pi,vi,a,t):
    y = ballistic2(pi,vi,a,t)
    fp = open( 'data.csv', 'a' )
    fp.write( str(t) + "," + str(y) + "\n" )
    fp.close()
    print(t,",",y)
computeAndOutput(2,11,-10,0.5)

def trajectory10(pi,v,a,step,ti,):
    for N in range(0,10):
        computeAndOutput(pi,v,a,ti + (N * step))

print("trajectory10 test run:")    
trajectory10(1,11,-10,.1,0)

def trajectory100(pi,v,a,step,ti): 
    for N in range(0,100):
        computeAndOutput(pi,v,a,ti + (N * step))

print("trajectory100 test run")
trajectory100(1,50,-10,.1,0)

def trajectory1000(pi,v,a,step,ti):
    for N in range(0,1000):
        computeAndOutput(pi,v,a,ti + (N * step))

trajectory1000(1,50,-10,.1,0)

def clearfile():
    fp = open( 'data.csv', 'w' )
    fp.close()
clearfile()