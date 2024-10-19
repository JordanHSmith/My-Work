'''
Jordan Smith
Fall 2021
CS 152 Project 2
This program prints the highest and lowest air temperature
    and water temperature at 3m
To run in terminal, type "python3 temps.py"
'''
fp = open("GoldieMLRCJuly.csv","r")

def main():
    '''
    No parameters
    No return value
    Prints the highest and lowest air temperature and water
        temperature at 3m
    '''


    line = fp.readline()
    highest_water_temp = 0
    lowest_water_temp = 1000
    highest_water_temp_date = ""
    lowest_water_temp_date = ""
    current_water_temp = 0

    highest_air_temp = 0
    lowest_air_temp = 100
    highest_air_temp_date = ""
    lowest_air_temp_date = ""
    current_air_temp = 0

    for line in fp:
        words = line.split(",")

        
        current_water_temp = float(words[1])
        #Makes current_water_temp the highest_water_temp if it is the bigger of the two
        if(current_water_temp > highest_water_temp): 
            highest_water_temp = current_water_temp
            highest_water_temp_date = words[0]
        
        #Makes current_water_temp the lowest_water_temp if it is the smaller of the two
        if(current_water_temp < lowest_water_temp):
            lowest_water_temp = current_water_temp
            lowest_water_temp_date = words[0]

        current_air_temp = float(words[5])
        #Makes current_air_temp the highest_air_temp if it is the bigger of the two
        if(current_air_temp > highest_air_temp):
            highest_air_temp = current_air_temp
            highest_air_temp_date = words[0]
        #Makes current_air_temp the lowest_air_temp if it is the smaller of the two
        if(current_air_temp < lowest_air_temp):
            lowest_air_temp = current_air_temp
            lowest_air_temp_date = words[0]
    fp.close()

    highest_water_temp = (str)(highest_water_temp)
    lowest_water_temp = (str)(lowest_water_temp)

    highest_air_temp = (str)(highest_air_temp)
    lowest_air_temp = (str)(lowest_air_temp)

    print("The highest water temperature of " + highest_water_temp 
    + " degrees Celsius at 3m occurred on " + highest_water_temp_date + ".")
    print("The lowest water temperature of " + lowest_water_temp 
    + " degrees Celsius at 3m occurred on " + lowest_water_temp_date + ".")

    print("The highest air temperature of " + highest_air_temp 
    + " degrees Celsius occurred on " + highest_air_temp_date + ".")
    print("The lowest air temperature of " + lowest_air_temp 
    + " degrees Celsius occurred on " + lowest_air_temp_date + ".")

main()