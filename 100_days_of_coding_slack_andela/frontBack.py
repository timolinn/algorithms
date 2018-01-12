'''
Created on Jan 14, 2017

@author: User
'''
def front_back(a, b):
    assert type(a) == str and type(b) == str
    
    try:
        if len(a) % 2 == 0 and len(b) % 2 == 0:
            half1A, half1B = a[:int(len(a)/2)], b[:int(len(b)/2)]
            half2A, half2B = a[int(len(a)/2):], b[int(len(b)/2):]
            return half1A + half1B + half2A + half2B
        elif len(a) % 2 != 0 and len(b) % 2 == 0:
            half1A, half1B = a[:int((len(a)+1)/2)], b[:int(len(b)/2)]
            half2A, half2B = a[int((len(a)+1)/2):], b[int(len(b)/2):]
            return half1A + half1B + half2A + half2B
        elif len(a) % 2 == 0 and len(b) % 2 != 0:
            half1A, half1B = a[:int(len(a)/2)], b[:int((len(a)+1)/2)]
            half2A, half2B = a[int(len(a)/2):], b[int((len(a)+1)/2):]
            return half1A + half1B + half2A + half2B
        else:
            half1A, half1B = a[:int((len(a)+1)/2)], b[:int((len(a)+1)/2)]
            half2A, half2B = a[int((len(a)+1)/2):], b[int((len(a)+1)/2):]
            return half1A + half1B + half2A + half2B
    except (AssertionError):
        raise AssertionError("Invalid input")
       
    
    
    
def main():    
    print(front_back(123, 'yzr')) # SHOULD RETURN 'abcxydez'
    
if __name__ == "__main__": main()