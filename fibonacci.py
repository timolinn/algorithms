'''
Created on Nov 24, 2016

@author: User
'''
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def duplicate_count(text):
    # Your code goes here
    lt = []
    if not isinstance(text, str):
        return "Invalid input"
    else:
        count = 0
        text = text.split(",")
        for i in text:
            text = lt.append(i)
            for i in range(0, len(text)):
                for x in range(0, len(text)):
                    if x == i:
                        count += 1
        return count

#class Memoize:
    #def __init__(self, fn):
      #  self.fn = fn
     #   self.memo = {}
    #def __call__(self, *args):
        #if args not in self.memo:
        #self.memo[args] = self.fn(*args)
        #return self.memo[args]
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

n = input("Enter a number \n")
n = int(n); index = 1; c = 1
while c <= n :
    print(str(c))
    index = index+1
    c = fibonacci(index)

def main():
    
    print(fib(70))
    print(duplicate_count("aassjdoocjxoxoop"))
    
    
if __name__ == "__main__": main()