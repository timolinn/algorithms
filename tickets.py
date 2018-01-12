#!/usr/bin/python3
'''
Created on Nov 23, 2016

@author: User
'''

def tickets(people):
    change = 'YES'
    twentyfive, fifty, onehundred = 0, 0, 0
    
    for cash in people:
        if change == 'NO':
            break

        if cash == 25:
            twentyfive += 1
        elif cash == 50 and twentyfive > 0:
            twentyfive -= 1
            fifty += 1
        elif cash == 100:
            if fifty > 0 and twentyfive > 0:
                fifty -= 1
                twentyfive -= 1
                onehundred += 1
            elif twentyfive > 2:
                twentyfive -= 3
                onehundred += 1
            else:
                change = 'NO'
        else:
            change = 'NO'
            
    return change
    
           
   
def main():    
    print(tickets([25, 25, 50]))
    
    
    
if __name__ == "__main__": main()