#!/usr/bin/python3

'''
Created on Nov 20, 2016

@author: User
'''
from math import ceil

def series_sum(n):
    # Happy Coding ^_^
    num, denom = 1, 1
    numList = []
    while n >= 1:
        numList.append(num/denom)
        denom += 3
        n -= 1
    total = sum(numList)
    return('{:.2f}'.format(total))

'''ALTERNATIVELY
    def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
'''
    
def main():
    print(series_sum(58))
    
if __name__== "__main__": main()
