'''
Jordan Smith
09/29/21
CS152B
'''

import random
import matplotlib.pyplot as plt

def getNrandom(N):
    numbers = []

    for i in range(N):
        numbers.append(random.random())
    return numbers

def getNintegers(N, lower_bound, upper_bound):
    numbers = []
    for i in range(N):
        numbers.append(random.randint(lower_bound, upper_bound))
    return numbers

def getNnormal(N, mean, standard_deviation):
    numbers = []
    for i in range(N):
        numbers.append(random.gauss(mean,standard_deviation))
    return numbers

def test():
    x = getNrandom(10)
    y = getNintegers(10,-10,10)
    z = getNnormal(10,0,.2)

    for i in range(len(x)):
        print(x[i])
        print(y[i])
        print(z[i])
    plt.plot(x,z,'o')
    plt.title("My First Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


test()
