'''
Created on Jan 7, 2017

@author: User
'''

def fib(val):
    if not isinstance(val, int) or val < 0:
        return "Function must be called with an a positive Integer"
    elif val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        a, b = 0, 1
        while b <= val:
            yield b
            a, b = b, a + b

def printFib(val):
    for x in fib(val):
        if x > val: break
        print(x)
    

    
class Fibonacci():
    def __init__(self, val):
        self.val = int(val)
        
    def series(self, a = 0, b = 1):
        self.a = a
        self.b = b
        while self.b <= self.val:
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b
    
            
#value = int(input("Enter Integer: "))
#f = Fibonacci(value)
#for r in f.series():
  #  if r > value: break    
  #  print(r, end=' ')
  
yourNumber = input("Give me your number: ")
yourNumber = int(yourNumber)
x = 0
y = 1
while y <= yourNumber:
    print(y, end = ",")
    temp1 = y
    temp2 = x + y
    x = temp1
    y = temp2  
    
    
    
        
#def main():
    #fibonacci()
 #   printFib(2)
    


#if __name__ == "__main__": main()
        
        