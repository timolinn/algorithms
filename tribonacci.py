'''
Created on Nov 22, 2016

@author: User
'''
def tribonacci(signature,n):
    #your code here
    a = signature[0]
    b = signature[1]
    c = signature[2]
    if n == 1:
        print([1])
    elif n == 0: return []
    else:
        if n > 3: n-= 3
        while n >= 1:
            d = a + b + c
            signature.append(d)
            n -= 1
            a, b, c, d = b, c, d, a + b + c
            
    print(signature)

def main():
    tribonacci([4,13,18], 3)   
    
    
    
#other ppls code
def fribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res 
    
#xbonacci takes any number of arguements
def Xbonacci(signature,n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output
    
    
if __name__ == "__main__": main()
    
    
    