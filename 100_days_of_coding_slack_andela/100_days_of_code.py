'''
Created on Jan 4, 2017

@author: User
'''
def mod_exp(a, b, c):
  f = 1
  x = []
  y = []
  while f <= b:
    if f == 1:
      m = a%c
    else:
      m = (m * m)%c
    y.append(m)
    x.append(f)
    f = f * 2
  count = len(y)  
  q = 1 
  while count > 0:
    t = x.pop()
    count -= 1
    if (b - t) >= 0:
      q = q * y[count] 
      b -= t  
  return q%c   
  
  
# This module uses fast modular exponentiation (repeating square technique) to compute powers in 0(log n) time
import math

def mod_pow(a, b, c):
    solution = []  # holds the power multiples
    power = bin(b).lstrip('0b')  # converts the power to binary format
    length = len(power)  # gets the length of the string power
    answer = 1
    solution.append(a)
    for x in range(length-1):  # repeated square implementation
        a *= a
        a %= c
        solution.append(a)
    for y in range(0,len(solution)):
        if power[y] == '1':
            answer *= solution[len(solution)-y-1]
            answer %= c
    return answer


def input_validator(a, b, c):
    try:
        int(a)
        int(b)
        int(c)
        return "valid"
    except:
        return "invalid"

# code execution starts here

import time, datetime   #for timing purposes only

def is_int(num):   #to test if given number is an integer
  try:
    int(num)
    return True
  except ValueError:
    print (num + " is not an integer. ",)  
    return False

def exponential_modulo(a, b, c): #our main function
  t0 = time.clock() #start clock
  a, b, c = int(a), int(b), int(c) 
  if b < 0:   #take care of negative powers
    a = 1 / a
    b = -b
  if b == 0:   #take care of zero power
    return 1
  y = 1
  while b > 1:
    if b % 2 == 0:    #for even powers
      a = (a * a) % c
      b /=2
    else:    #for odd powers
      y *= a
      a *= a
      a = (a * y) % c
      b = (b-1)/2
  t1 = time.clock() #stop clock
  print ("Time taken = ", t1 - t0, " seconds, and the answer is: " + str(a))
  return a

#user test
a = input("Enter a base integer ")
b = input("Raised to? Enter an integer ")
c = input("Enter mod integer. Must not be zero ") 
if is_int(a) and is_int(b) and is_int(c) and c != 0:
  exponential_modulo(a, b, c)
else:
  print ("Invalid input")
  
  
  
'''def main():
    #print(mod_exp(5, 117, 19))
    exponential_modulo(5, 117, 19)
    
    
if __name__ == "__main__" : main()'''


def main():
    #print(mod_exp(5, 117, 19))
    a = input("Enter base number\n")
    b = input("Enter power\n")
    c = input("Enter mod\n")
    input_validator(a, b, c)
    if input_validator(a, b, c) == "valid":
        a = int(a)
        b = int(b)
        c = int(c)
        if a < 1:
            print("Base a must be greater than zero")
        elif b < 0:
            print("power b must be positive")
        else:
            print(mod_pow(a, b, c))
    else:
        print("Invalid number/numbers")
#print(pow(a, b, c))
    
    
if __name__ == "__main__" : main()