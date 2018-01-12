'''
Created on Jan 6, 2017

@author: User
'''

printValues = ["FizzBuzz", "Fizz", "Buzz"]

for i in range(1,101):
    if i % 3 == 0  and i % 5 == 0:
        print(printValues[0])
    elif i % 3 == 0:
        print(printValues[1])
    elif i % 5 == 0:
        print(printValues[2])
    else:
        print(i) 