'''Jordan Smith
09/14/21
CS 152 B
Project 01'''

print('version 1')
print('sum', 42 + 21 + 5)
print('avg', (42 + 21 + 5) / 3)
def myfunction(a,b,c):
    print('sum', a + b + c)
myfunction(4,5,6)
myfunction(3,18,7)

print('version 2')
print('sum', 42 + 21 + 5)
print('avg', (42 + 21 + 5) // 3)
def myfunction(a,b,c):
    print('sum', a + b + c)
myfunction(4,5,6)

print('version 3')
print('sum', 42 + 21 + 5.0)
print('avg', (42 + 21 + 5) // 3.0)
def myfunction(a,b,c):
    print('sum', a + b + c)
myfunction(4,5,6)

print('version 4')
a = 42
b = 21
c = 5
print('sum', a + b + c)
print('avg', (a + b + c) / 3.0)
def myfunction(a,b,c):
    print('sum', a + b + c)
myfunction(4,5,6)

print('version 5')
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")
a = int(a)
b = int(b)
c = int(c)
print('sum', a + b + c)
print('avg', (a + b + c) / 3.0)
def myfunction(a,b,c):
    print('sum', a + b + c)
myfunction(4,5,6)
myfunction(3,6,5)

print('version 6')
def stats(a,b,c):
    print('sum', a + b + c)
stats(42,21,5)
stats(38,64,9)