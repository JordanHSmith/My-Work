'''
Jordan Smith
09/22/21
CS 152
Adds the ability to determine the range, median, and mode of a list
'''

def sum(numbers): 
    '''Returns the sum of all items in numbers
    (list) -> (float)'''
    sum = 0.0

    for num in numbers:
        sum += num
    return(sum)

#
def test():
    '''Tests the sum function
    No Parameters'''
    number_list = [1, 2, 3, 4]
    final_sum = sum(number_list)
    print(final_sum)

def mean(data):
    '''Returns the mean of the items in data
    (list) -> (float)'''
    mean = sum(data) / len(data)
    return(mean)

def min(data):
    '''Returns the minimum of the items in data
    (list) -> (float)'''
    min = data[0]
    for num in data:
        if(num < min):
            min = num
    return(min)

def max(data):
    '''Returns the maximum of the items in data
    (list) -> (float)'''
    max = data[0]
    for num in data:
        if(num > max):
            max = num
    return(max)

def variance(data):
    '''Returns the variance between the items in data
    (list) -> (float)'''
    squared_differences = []
    for num in data:
        squared_differences.append(pow(num - mean(data), 2))
    variance = (sum(squared_differences) / (len(data) - 1))
    return(variance)

def find_range(data):
    '''Returns the range of the items in data
    (list) -> (float)'''
    sorted_list = sorted(data)
    range_distance = sorted_list[len(data)-1] - sorted_list[0]
    return(range_distance)

def median(data):
    '''Returns the median item in data. If data has an even number of items,
    median is made equal to the average of the two middle terms.
    (list) -> (float)'''
    median = 0
    sorted_list = sorted(data)
    if(len(sorted_list) % 2 == 0):
        median = (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2
    else:
        median = sorted_list[len(sorted_list) // 2]
    return(median)

def mode(data):
    '''Returns a list of the mode(s) in data
    (list) -> (list)'''
    sorted_list = sorted(data)
    most_common_number = []
    occurance = 0
    max_occurance = 0
    for i in range(1,len(sorted_list)):
        if(sorted_list[i] == sorted_list[i-1]):
            occurance += 1
            if(occurance > max_occurance):
                most_common_number = []
                most_common_number.append(sorted_list[i])
                max_occurance = occurance
            elif(occurance == max_occurance):
                most_common_number.append(sorted_list[i])
        else:
            occurance = 0
    if(most_common_number == []):
        return("There is not a mode in this data.")
    return(most_common_number)

if __name__ == "__main__":
    test()
    print("Mean: " + (str)(mean([1, 54, 67.0, -2])))
    print("Max: " + (str)(max([1, 54, 67.0, -2])))
    print("Min: " + (str)(min([1, 54, 67.0, -2])))
    print("Variance: " + (str)(variance([1, 54, 67.0, -2])))
    print("Range: " + (str)(find_range([1, 54, 67.0, -2])))
    print("Median " + (str)(median([1, 54, 67.0, -2]))) #Tests median function with an even amount of numbers
    print("Median " + (str)(median([1, 54, 67.0, -2, 8]))) #Tests median function with an odd amount of numbers
    print("Mode: " + (str)(mode([1, 54, 67.0, -2]))) #Tests mode function with no mode
    print("Mode: " + (str)(mode([1, 54, 67.0, -2, 67.0]))) #Tests mode function for when there is one mode
    print("Mode: " + (str)(mode([1, 54, 67.0, -2, 67.0, 54]))) #Tests mode function for when there are two modes