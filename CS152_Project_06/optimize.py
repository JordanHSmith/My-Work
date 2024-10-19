'''
Jordan Smith
10/26/21
CS 152
Returns a list of tuples containing altered values for an inputted parameter and
    the corresponding ideal darting percentage.
To run in terminal type "python3 optimize.py"
'''

import sys
import elephant
import random

def optimize(min,max,optfunc,parameters = None,tolerance = 0.001,maxIterations = 20,verbose = False):
    '''
    (float,float,function,list,float,int,boolean) -> float
    Returns the optimal darting percentage for a given range of values
    '''

    done = False

    #Uses the binary search technique to find the ideal darting percentage
    while(done == False):
        testValue = (max+min) / 2
        if(verbose):
            print(testValue)
        result = optfunc(testValue,parameters)
        if(verbose):
            print(result)
        if(result > 0):
            max = testValue
        elif(result < 0):
            min = testValue
        else:
            done = True
        if(max-min < tolerance):
            done = True
        maxIterations -= 1
        if(maxIterations <= 0):
            done = True

    return(testValue)

# a function that returns x - target
def target(x, pars):
    return x - 0.73542618

# Tests the binary search using a simple target function.
# Try changing the tolerance to see how that affects the search.
def testTarget():
    res = optimize(0.0, 1.0, target, tolerance = 0.01, verbose=True)
    print(res)
    return



def testEsim():
    '''
    No parameters or return
    Prints out an example of the optimize function.
    '''
    res = optimize(0.0,0.5,elephant.elephantSim,verbose=True)
    print(res)
    return


def evalParameterEffect( whichParameter, testmin, testmax, teststep, defaults=None, verbose=False ):
    '''
    (int,float,float,float,list,boolean) -> (list)
    Returns a list of tuples containing an incremented value of some given parameter and
        its corresponding ideal darting percentage.
    '''
    
    if(defaults == None):
        simParameters = elephant.defaultParameters()
    else:
        simParameters = defaults[:]
    
    results = []

    if verbose:
        print ("Evaluating parameter %d from %.3f to %.3f with step %.3f" % (whichParameter, testmin, testmax, teststep))
        t = testmin
    while(t < testmax):
        simParameters[whichParameter] = t
        percDart = optimize(0,1,elephant.elephantSim,parameters = simParameters)
        results += (t,percDart)
        if verbose:
            print ("%8.3f \t%8.3f" % (t, percDart))
        t += teststep
    if(verbose):
        print("Terminating")

    return(results)
            
    


if __name__ == "__main__":
    evalParameterEffect( elephant.IDXProbabilityofAdultSurvival, 0.98, 1.0, 0.001, verbose=True )
    #evalParameterEffect( elephant.IDXProbabilityofCalfSurvival, 0.80, 0.90, 0.01, verbose=True )
    #evalParameterEffect( elephant.IDXProbabilityofSeniorSurvival, 0.1, 0.5, 0.05, verbose=True )
    # evalParameterEffect( elephant.IDXCalvingInterval, 3.0, 3.4, 0.05, verbose=True )
    #evalParameterEffect( elephant.IDXMaximumAge, 56, 66, 2, verbose=True )

    #This is my extension code, which analyzes the effect the carrying capcity has on
        #the optimal darting percentage
    # evalParameterEffect( elephant.IDXCarryingCapacity, 1, 1500, 100, verbose=True )
    # testEsim()