#!/usr/bin/python3
'''
Created on Nov 20, 2016

@author: User
'''


import string

def printer_error(s):
    error_color = string.ascii_lowercase[13:]
    denom = len(s)
    numera = 0
    for t in s:
        if t in error_color:
            numera += 1
    return ("{}/{}".format(str(numera), str(denom)))

def main():
    print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
    
    
if __name__ == "__main__": main()