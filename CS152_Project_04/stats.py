'''
Jordan Smith
09/22/21
CS 152
Provides many functions to calculate various statistics
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

if __name__ == "__main__":
    test()
    print("Mean: " + (str)(mean([1, 54, 67.0, -2])))
    print("Max: " + (str)(max([1, 54, 67.0, -2])))
    print("Min: " + (str)(min([1, 54, 67.0, -2])))
    print("Variance: " + (str)(variance([1, 54, 67.0, -2])))