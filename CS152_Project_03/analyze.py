'''
Jordan Smith
09/22/21
CS 152
Returns various statistics about a file input in the terminal
'''

import sys
import stats

def main(filename, column_id):

# assign to fp the result of opening the file hurricanes.csv for reading
    fp = open(filename, "r")
# assign to line the first line of the data file
    line = fp.readline()
# assign to headers the result of splitting the line using commas
    headers = line.split(",")
# print headers
    print(headers)

# assign to data an empty list
    data = []

# for all of the lines in the file
    for line in fp:
        # assign to words the result of splitting the line using commas
        words = line.split(",")
        # append second item to data (which index?) in words cast as a float
        data.append(float(words[column_id]))
    data_sum = stats.sum(data)
    data_mean = stats.mean(data)
    data_max = stats.max(data)
    data_min = stats.min(data)
    data_variance = stats.variance(data)
    # close the data file
    fp.close()
    # print data
    print("sum: " + "{:.2f}".format(data_sum))
    print("mean: " + "{:.2f}".format(data_mean))
    print("max: " + "{:.2f}".format(data_max))
    print("min: " + "{:.2f}".format(data_min))
    print("variance: " + "{:.2f}".format(data_variance))
    return 

if __name__ == "__main__":
    main(sys.argv[1],(int)(sys.argv[2]))
