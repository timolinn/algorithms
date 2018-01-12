'''
Created on Jan 10, 2017

@author: User
'''

def mix_up(a,b):
    a, b = str(a).strip(), str(b).strip() #remove all leading and trailing spaces
    
    if len(a) < 2 and len(b) < 2:
        return "Your string is too short"
    else:
        a, b = list(a), list(b)
        first2CharsA = a[:2] #initialize new list with the first two chars of the string
        first2CharsB = b[:2]
        
        for i in range(2): #removes the first two chars of the string
            a.pop(0)
            b.pop(0)
        
        for j in a:
            first2CharsB.append(j)
        
        for k in b:
            first2CharsA.append(k)
       
        a = ''.join(first2CharsB)
        b = ''.join(first2CharsA)
    
    return str(a + " " + b)


def main():
    print(mix_up("mix", "pod"))
    
if __name__ == "__main__": main()
        