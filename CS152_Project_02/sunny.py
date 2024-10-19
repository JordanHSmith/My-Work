'''
Jordan Smith
09/21/21 2021
CS 152 Project 2
This program prints the number of sunny and cloudy days in August
    as well as the average PAR value for all the sunny days
    and all the cloudy days, respectively.
To run in terminal, type "python3 sunny.py"
'''

fp = open("GoldieMLRCJuly.csv","r")

def main():
    '''
    No parameters
    No return value
    Prints the number of sunny and cloudy days in August at
        12:03PM as well as the average PAR value for all the
        sunny days and all the cloudy days, respectively.
    '''

    line = fp.readline()
    par_value = 0
    sunny_day_counter = 0
    cloudy_day_counter = 0
    sunny_day_par_sum = 0
    cloudy_day_par_sum = 0
    sunny_day_par_average = 0
    cloudy_day_par_average = 0

    for line in fp:
        words = line.split(",")
        par_value = float(words[4])
        #Determines whether it is sunny or cloudy based on PAR at 12:03PM
        if("12:03" in words[0]):
            if(par_value > 800):
                sunny_day_counter += 1
                sunny_day_par_sum += par_value
            else:
                cloudy_day_counter += 1
                cloudy_day_par_sum += par_value
    
    sunny_day_par_average = sunny_day_par_sum / sunny_day_counter
    cloudy_day_par_average = cloudy_day_par_sum / cloudy_day_counter

    sunny_day_counter = (str)(sunny_day_counter)
    cloudy_day_counter = (str)(cloudy_day_counter)
    sunny_day_par_average = (str)(sunny_day_par_average)
    cloudy_day_par_average = (str)(cloudy_day_par_average)

    print("There were " + sunny_day_counter + " sunny days in July.")
    print("There were " + cloudy_day_counter + " cloudy days in July.")
    print("The average PAR on a sunny day was " + sunny_day_par_average)
    print("The average PAR on a cloudy day was " + cloudy_day_par_average)

main()