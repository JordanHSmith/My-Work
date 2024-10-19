'''
Jordan Smith
10/19/21
CS 152
Simulates an Elephant reservation with an emphasis on population control
To run in terminal type "python3 elephant.py " followed by the probability of
    darting. This number should be between 0 and 1 (exclusive).
'''

import random
import sys

IDXCalvingInterval = 0
IDXPercentDarted = 1
IDXJuvenileAge = 2
IDXMaximumAge = 3
IDXProbabilityofCalfSurvival = 4
IDXProbabilityofAdultSurvival = 5
IDXProbabilityofSeniorSurvival = 6
IDXCarryingCapacity = 7
IDXNumberofYears = 8
IDXNumYears = 9

IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3

def test():
    #test() has no paramters and does not return anything.
    #This function is intended to print out an elephant population before and after
        #running the incrementAge function in order to demonstrate it works properly.

    calving_interval = 3.1
    percent_darted = 0.0
    juvenile_age = 12
    maximum_age = 60
    probability_of_calf_survival = 0.85
    probability_of_adult_survival = 0.996
    probability_of_senior_survival = 0.20
    carrying_capacity = 20
    number_of_years = 200
    num_years_run = 50

    
    par_list = [calving_interval,percent_darted,juvenile_age,
    maximum_age,probability_of_calf_survival,probability_of_adult_survival,
    probability_of_senior_survival,carrying_capacity,number_of_years,num_years_run]

    print(par_list)

    pop = []
    parameters = par_list
    for i in range(15):
        pop.append( newElephant( parameters, random.randint(1, parameters[IDXMaximumAge]) ))

    for e in pop:
        print(e)

    print(initPopulation(par_list))

    pop_list = initPopulation(par_list)
    pop = pop_list
    print("ONE")
    print(pop)
    print("TWO")
    pop = incrementAge(pop_list)
    print(pop)



def newElephant( parameters, age ):
    '''
    (list,int) -> (list)
    Returns a list of attributes of a newly made elephant.
    '''

    elephant = [0,0,0,0]

    #Provides attributes for an elephant depending upon its given age and randomly
        #selected gender. The two internal if-statements determine if and for how
        #long the elephant is/has been pregant.
    elephant[IDXGender] = random.choice(["m","f"])
    elephant[IDXAge] = age
    if('f' in elephant[IDXGender]):
        if(elephant[IDXAge] > parameters[IDXJuvenileAge] and elephant[IDXAge] < parameters[IDXMaximumAge]):
            if(random.random() < (1/parameters[IDXCalvingInterval])):
                elephant[IDXMonthsPregnant] = random.randrange(1,23)

    return elephant

def initPopulation(paramlist):
    '''
    (list) -> (list)
    Takes in the parameter list and returns a list of elephants the length
        of the carrying capacity.
    '''
    pop = []
    for i in range(paramlist[IDXCarryingCapacity]):
        pop.append(newElephant(paramlist, random.randrange(1,paramlist[IDXMaximumAge])))
    
    return(pop)

def incrementAge(population):
    '''
    (list) -> (list)
    Takes in a population list and returns a population list with older elephants.
    '''
    pop = list(population)
    for i in range(len(pop)):
        pop[i][IDXAge] += 1

    return(pop)

def calcSurvival(param_list, pop_list):
    '''
    (list,list) -> (list)
    Returns a list of elephants who survive based on their age group's probability of survival.
    '''

    new_population = []
    for e in pop_list:
        if(e[IDXAge] < 2):
            if(random.random() < param_list[IDXProbabilityofCalfSurvival]):
                new_population.append(e)
        elif(e[IDXAge] <= 60):
            if(random.random() < param_list[IDXProbabilityofAdultSurvival]):
                new_population.append(e)
        else:
            if(random.random() < param_list[IDXProbabilityofSeniorSurvival]):
                new_population.append(e)
    return(new_population)

def dartElephants(param_list, pop_list):
    '''
    (list,list) -> (list)
    This function returns an updated list of elephants with some newly darted ones.
    '''

    pop = pop_list
    prob_of_darting = param_list[IDXPercentDarted]
    juvenile_age = param_list[IDXJuvenileAge]
    max_age = param_list[IDXMaximumAge]

    #Randomly darts adult female elephants.
    for i in range(len(pop)):
        if('f' in pop[i][IDXGender] and pop[i][IDXAge] > juvenile_age and pop[i][IDXAge] < max_age):
            if(random.random() < prob_of_darting):
                pop[i][IDXMonthsPregnant] = 0
                pop[i][IDXMonthsContraceptiveRemaining] = 22
    
    return(pop)

def cullElephants(param_list, pop_list):
    '''
    (list,list) -> (tuple)
    Returns a tuple with a (potentially) culled elephant pop and the number culled.
    Culls off excess elephants if the population exceeds carrying capacity.
    '''
    carrying_capacity = param_list[IDXCarryingCapacity]

    if(len(pop_list) > carrying_capacity):
        cull_number = len(pop_list) - carrying_capacity
        random.shuffle(pop_list)
        new_pop = pop_list[:carrying_capacity]
    else:
        cull_number = 0
        new_pop = pop_list
    return(new_pop,cull_number)

def controlPopulation( parameters, population ):
    '''
    (list,list) -> (tuple)
    This function is meant to call the dartElphants and cullElephants functions
        under the appropriate circumstances.
    '''

    if(parameters[IDXPercentDarted] == 0):
        (newPop,numCulled) = cullElephants(parameters,population)
    else:
        dartElephants(parameters,population)
        numCulled = 0
        newPop = population
    return(newPop, numCulled)

def simulateMonth(param_list,pop_list):
    '''
    (list,list) -> (list)
    This function returns a new list with information related to reproduction now updated.
    '''
    calving_interval = param_list[IDXCalvingInterval]
    juvenile_age = param_list[IDXJuvenileAge]
    max_age = param_list[IDXMaximumAge]

    #Adjusts contraceptives, births, and conceptions for adult female elephants.
    for e in pop_list:
        gender = e[IDXGender]
        age = e[IDXAge]
        monthsPregnant = e[IDXMonthsPregnant]
        monthsContraceptive = e[IDXMonthsContraceptiveRemaining]

        if(gender == 'f' and age > juvenile_age and age < max_age):
            if(monthsContraceptive > 0):
                e[IDXMonthsContraceptiveRemaining] -= 1
            elif(monthsPregnant > 0):
                if(monthsPregnant >= 22):
                    pop_list.append(newElephant(param_list,1))
                    e[IDXMonthsPregnant] = 0
                else:
                    e[IDXMonthsPregnant] += 1
            else:
                if(monthsContraceptive == 0 and random.random() < (1.0 / (calving_interval*12 - 22))):
                    e[IDXMonthsPregnant] = 1
    return(pop_list)

def simulateYear(param_list,pop_list):
    '''
    (list,list) -> (list)
    This function pushes the simulation a year along.
    '''
    pop_list = calcSurvival(param_list,pop_list)
    pop_list = incrementAge(pop_list)
    for i in range(12):
        pop_list = simulateMonth(param_list,pop_list)
    return(pop_list)

def calcResults(param_list,pop_list,num_culled):
    '''
    (list,list,int) -> (int,int,int,int,int,int,int)
    Returns the number of specific groups of elephants (most age-based).
    '''
    calf_age = 2
    juvenile_age = param_list[IDXJuvenileAge]
    max_age = param_list[IDXMaximumAge]

    num_calves = 0
    num_juveniles = 0
    num_adult_males = 0
    num_adult_females = 0
    num_seniors = 0

    for e in pop_list:
        if(e[IDXAge] < calf_age):
            num_calves += 1
        elif(e[IDXAge] < juvenile_age):
            num_juveniles += 1
        elif(e[IDXAge] < max_age):
            if('f' in e[IDXGender]):
                num_adult_females += 1
            else:
                num_adult_males += 1
        else:
            num_seniors += 1

    return(len(pop_list), num_calves, num_juveniles, num_adult_males, num_adult_females, num_seniors, num_culled)

def runSimulation(parameters):
    '''
    (list) -> (list)
    This runs the whole simulation and stops it if the elephant population gets too large.
    '''
    popsize = parameters[IDXCarryingCapacity]

    # init the population
    population = initPopulation( parameters )
    [population,numCulled] = controlPopulation( parameters,
    population )
    # run the simulation for N years, storing the results
    results = []
    for i in range(parameters[IDXNumYears]):
        population = simulateYear( parameters, population )
        [population,numCulled] = controlPopulation( parameters, population )
        results.append( calcResults( parameters, population, numCulled ) )
        if results[i][0] > 2 * popsize or results[i][0] == 0 :
            # cancel early, out of control
            print( 'Terminating early' )
            break

    return results


def main(argv):
    '''
    This function takes in a float but has no return.
    The function is intended to print out the average number of the various
        groups of elephants, depdning upon what the input probability of darting is.
    '''


    probDart = float(argv[1])

    calving_interval = 3.1
    percent_darted = probDart
    juvenile_age = 12
    maximum_age = 60
    probability_of_calf_survival = 0.85
    probability_of_adult_survival = 0.996
    probability_of_senior_survival = 0.20
    carrying_capacity = 7000
    number_of_years = 200
    num_years_run = 50

    par_list = [calving_interval,percent_darted,juvenile_age,
    maximum_age,probability_of_calf_survival,probability_of_adult_survival,
    probability_of_senior_survival,carrying_capacity,number_of_years,num_years_run]

    results = runSimulation(par_list)

    total_e = 0
    total_calves = 0
    total_juveniles = 0
    total_adult_male = 0
    total_adult_female = 0
    total_seniors = 0
    total_culled = 0

    for result in results:
        total_e += result[0]
        total_calves += result[1]
        total_juveniles += result[2]
        total_adult_male += result[3]
        total_adult_female += result[4]
        total_seniors += result[5]
        total_culled += result[6]

    num_e = total_e / len(results)
    num_calves = total_calves / len(results)
    num_juveniles = total_juveniles / len(results)
    num_adult_male = total_adult_male / len(results)
    num_adult_female = total_adult_female / len(results)
    num_seniors = total_seniors / len(results)
    num_culled = total_culled / len(results)

    print("On average in any given year, there were", num_e, "total elphants,", num_calves, "calves,", num_juveniles, "juveniles,",
    num_adult_male, "adult male elephants,", num_adult_female, "adult female elephants,", num_seniors, "seniors, and",
    num_culled, "elephants were culled.")

if __name__ == "__main__":
    #test()
    main(sys.argv[1])