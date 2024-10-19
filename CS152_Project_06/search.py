'''
Jordan Smith
10/26/21
CS 152
Tests a basic binary search algorithm.
To run in terminal type "python3 search.py"
'''

import random

def searchSortedList( mylist, value ):
    '''
    (list,int) -> (tuple)
    Takes in a list and finds the target value. Returns a tuple containing
        a boolean for whether or not the target is found in addition to the
        number of times the code had to iterate to find the target.
    '''

    done = False
    found = False
    count = 0
    maxIdx = len(mylist) - 1
    minIdx = 0

    #Binary search algorithm to determine if and where target is in the list
    while(done != True):
        count += 1
        testIndex = (maxIdx + minIdx) // 2
        if(mylist[testIndex] < value):
            minIdx = testIndex + 1
        elif(mylist[testIndex] > value):
            maxIdx = testIndex - 1
        else:
            done = True
            found = True
        if(maxIdx < minIdx):
            done = True
            found = False

    return (found, count)


def test():
    '''
    No parameters or return
    Prints out the results of searchedSortedList to test it.
    '''
    a = []
    for i in range(10000):
        a.append( random.randint(0,100000) )
    a.append(42)
    a.sort()
    print(searchSortedList( a, 42 ))

if __name__ == "__main__":
    test()