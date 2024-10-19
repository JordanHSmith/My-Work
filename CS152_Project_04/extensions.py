'''
Jordan Smith
10/22/21
CS 152B
Prints out a list of extinction rates for a penguin population and makes a
    graph based on this data
To run in terminal, type "python3 penguin.py" then the number of times you
    wish to run the simulation and then how many years you want in between
    an El Nino event
'''

import random
import sys
import matplotlib.pyplot as plt


def initPopulation(init_size, prob_female):
    '''
    (int,float) -> (list)
    Takes in an intial population size and probability that a penguin
        will be female, the returns a list of either "m" for male
        or "f" for female
    '''

    population = []
    for i in range(init_size):
        if(random.random() < prob_female):
            population.append("f")
        else:
            population.append("m")
    return population

def simulateYear(pop, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity):
    '''
    (int,float,float,float,float,int,int) -> (list)
    Takes in various data related to the odds of survivability
        and then returns a list of a certain number of male and
        female penguins
    '''
    
    elNinoYear = False
    newpop = []
    
    if(random.random() < elNinoProb):
        elNinoYear = True

    #adjusts the penguin population according to whether the population
        #is less than the maximum capacity and whether it's an El Nino Year
    for penguin in pop:
        if(len(newpop) > maxCapacity):
            break
        if(elNinoYear):
            if(random.random() < elNinoRho):
                newpop.append(penguin)
        else:
            newpop.append(penguin)
            if(random.random() < stdRho - 1.0):
                if(random.random() < probFemale):
                    newpop.append("f")
                else:
                    newpop.append("m")
    return newpop


def runSimulation(N,initPopSize,probFemale,elNinoProb,stdRho,elNinoRho,maxCapacity,minViable):
    '''
    (int,int,float,float,float,float,int,int) -> (list)
    Runs the simulation, checking for whether the penguins go extinct and
        returns how many years the penguins survived
    '''
    
    pop = initPopulation(initPopSize,probFemale)
    endDate = N

    for i in range(N):
        newPop = simulateYear(pop,elNinoProb,stdRho,elNinoRho,probFemale,maxCapacity)
        if(len(newPop) < minViable or "f" not in newPop or "m" not in newPop):
            endDate = i
            break
        pop = newPop
    return endDate




# test function for initPopulations
def test():
    '''
    Test the simulation with hardcoded parameters
    '''
    popsize = 10
    probFemale = 0.5

    pop = initPopulation(popsize, probFemale)
    print( pop )

    newpop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)
    print( "El Nino year" )
    print( newpop )

    newpop = simulateYear(pop, 0.0, 1.188, 0.4, 0.5, 2000)
    print( "Standard year" )
    print( newpop )

    '''

    #runSimulation(201,500,.5,1.0/7.0,1.188,.41,2000,10)
    '''
    print("Begining: ")
    print(runSimulation(201,500,.5,1.0/7.0,1.188,.41,2000,10))
    print(runSimulation(201,500,.5,1.0/10.0,1.188,.41,2000,10))
    print(runSimulation(201,500,.5,3.5/7.0,1.188,.41,2000,10))

    return


def main(argv):
    '''
    (string,int,int) -> (list)
    Takes in the name of the program, the number of times the simulation
        is to be run, and the number of years between El Nino events.
        Prints a list of cumulative rates of extinction.
    '''

    if(len(argv) < 3):
        print("You must input at least three arguments.")
    
    numSims = (int)(argv[1])
    years_between_el_nino = (int)(argv[2])

    final_pop = []
    num_less_than_N = 0

    N = 201
    initPopSize = 500
    probFemale = .5
    stdRho = 1.188
    elNinoRho = .7
    maxCapacity = 2000
    minViable = 10

    for i in range(numSims):
        final_pop.append(runSimulation(N,initPopSize,probFemale,(1/years_between_el_nino),stdRho,elNinoRho,maxCapacity,minViable))
        if(final_pop[i] < N):
            num_less_than_N += 1

    print("The penguins have a " + str(num_less_than_N / numSims) + " probability of going extinct.")

    print(computeCEPD(final_pop,N))
    for i in range(0,len(computeCEPD(final_pop,N)),10):
        print(computeCEPD(final_pop,N))
        


def computeCEPD(results_list, N):
    '''
    (list,int) -> (list)
    Takes in a list of penguin populations and the number of years being
        analyzed, then returns a list of cumulative extinction rates.
    '''

    CEPD_list = []

    for i in range(N):
        CEPD_list.append(0)

    print("results-list: " + str(len(results_list)))
    print("CEPD_list: " + str(len(CEPD_list)))
    print("N: " + str(N))

    #Adds 1 to every population greater than a population which went extinct
    for num in results_list:
        if(num < N):
            for j in range(num,N):
                CEPD_list[j] += 1

    for i in range(len(CEPD_list)):
        CEPD_list[i] = CEPD_list[i] / len(results_list)
    print(CEPD_list)
    
    x = []
    for i in range(N):
        x.append(i)

    plt.plot(x,CEPD_list,'o')
    plt.axis([0,200,0,1.0])
    plt.title("Extinction Rate vs. Time")
    plt.xlabel("Time (Years)")
    plt.ylabel("Extinction Rate")
    plt.show()

    return(CEPD_list)


if __name__ == "__main__":
    test()
    main(sys.argv)