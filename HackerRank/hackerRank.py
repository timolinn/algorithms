'''
Created on Jan 7, 2017

@author: User
'''
import sys


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split()
    n,c,m = int(n),int(c),int(m)
    
if 1 <= t <= 1000:
    for i in range(1, t+1):
        if 2 <= n <= 1000000:
            if 1 <= c <= n:
                if 2 <= m <= n:
                    totalChocBought = n / c
                    extraChoc = totalChocBought / m
                    totalChocEaten = totalChocBought + extraChoc
    print (totalChocEaten)