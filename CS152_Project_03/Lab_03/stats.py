'''
Jordan Smith
09/22/21
CS 152
'''

def sum(numbers):
    sum = 0.0

    for num in numbers:
        sum += num
    return(sum)

def test():
    number_list = [1, 2, 3, 4]
    final_sum = sum(number_list)
    print(final_sum)

def mean(data):
    mean = sum(data) / len(data)
    return(mean)

def min(data):
    min = data[0]
    for num in data:
        if(num < min):
            min = num
    return(min)

def max(data):
    max = data[0]
    for num in data:
        if(num > max):
            max = num
    return(max)

def variance(data):
    squared_differences = []
    for num in data:
        squared_differences.append(pow(num - mean(data), 2))
    variance = (sum(squared_differences) / (len(data) - 1))
    return(variance)

if __name__ == "__main__":
    test()
    print(mean([1, 54, 67.0, -2]))
    print(max([1, 54, 67.0, -2]))
    print(min([1, 54, 67.0, -2]))
    print(variance([1, 54, 67.0, -2]))