'''
Jordan Smith
Fall 2019
CS 152 Project 2
'''

# any required import statements here

# main function here
def main():
    # main code here
    hi_temp = -200
    hi_date = ""


    fp = open("blend.csv", "r")
    line = fp.readline()
    for line in fp:
        words = line.split(",")
        temp = float(words[3])
        date = words[0]
        if(temp > hi_temp):
            hi_temp = temp
            hi_date = date
    print(str(hi_temp))
    print("Highest Temp: %f" % (hi_temp))
    print("Highest Temp: %.3f" % (hi_temp))
    print("Highest Temp: %7.3f" % (hi_temp))
    print("The highest temperature of %.3f occurred on %s." % (hi_temp,hi_date))

    print(hi_date)
    fp.close()




if __name__ == "__main__":
    main()
