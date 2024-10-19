'''
Jordan Smith
09/21/21 2021
CS 152 Project 2
This program prints the average wind speed in July
To run in terminal, type "python3 wind_average.py"
'''

fp = open("GoldieMLRCJuly.csv","r")

def main():
    '''
    No parameters
    No Return Value
    Prints the average wind speed in July ay 7:03AM
    '''

    line = fp.readline()
    wind_speed = 0
    wind_speed_sum = 0
    wind_speed_average = 0

    for line in fp:
        words = line.split(",")
        wind_speed = float(words[6])
        if(" 7:03" in words[0]):
            wind_speed_sum += wind_speed

    wind_speed_average = str(wind_speed_sum/31)
    print("The average wind speed at 7:03AM in July was " + wind_speed_average)

main()
        


