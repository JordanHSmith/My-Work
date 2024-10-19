'''
Jordan Smith
09/21/21 2021
CS 152 Project 2
This program prints the average wind speed in July
To run in terminal, type "python3 Project2_extensions2.py"
'''

fp = open("GoldieMLRCJuly.csv","r")

def main():
    '''
    No parameters
    No Return Value
    Prints the average wind speed in July using all available data points
    '''

    line = fp.readline()
    wind_speed = 0
    wind_speed_sum = 0
    wind_speed_average = 0

    for line in fp:
        words = line.split(",")
        wind_speed = float(words[6])
        wind_speed_sum += wind_speed

    wind_speed_average = str(wind_speed_sum/(31*(24*4))) #Denominator is total number of datapoints taken.
    print("The average wind speed in July was " + wind_speed_average)

main()