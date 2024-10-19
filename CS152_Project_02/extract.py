'''
Jordan Smith
09/08/21 2021
CS 152 Project 2
Creates a csv file with with the day of the month and the corresponding air temp at 3PM
'''

fp = open("GoldieMLRCJuly.csv","r")

def main():
    '''
    No Parameters
    No Return Value
    Extracts the air temp at 3PM for every day of July
    '''

    line = fp.readline()
    day = 1
    fw = open("extract.csv","w")
    fw.write("Day, " + "T3PM Temp" + '\n')
    for line in fp:
        words = line.split(",")
        if("15:03" in words[0]):
            fw.write(str(day) + ", " + words[5] + '\n')
            day += 1
    fp.close()
    fw.close()

main()