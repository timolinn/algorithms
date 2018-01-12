'''
Created on Jan 5, 2017

@author: User
'''
from iter_recur import replicate_recur

'''def pig_latin(word):
    temp = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    addition = ""
    for vowel in vowels:
        if temp[0] == vowel:
            count += 1
    if count >0:
        return "".join(temp)+"way"
    else:
            while count == 0 and len(temp) > 0:
                temp_count = 0
                for vowel in vowels:
                    if vowel == temp[0]:
                        count = 1
                        break
                if count > 0:
                    break
                addition+=temp[0]
                del(temp[0])
    return "".join(temp)+addition+"ay"

words = input("Enter a word\n")
print(pig_latin(words))'''

'''pyg = 'ay'
original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    if word[0] in 'aeiou':
        new_word = word + 'way'
        print(new_word)
    else:
        new_word = word+word[0]+pyg 
        new_word = new_word[1:]
        print (new_word)
else:
    print ('Type in a word, please!')'''
    
'''a = input("Enter first word: ")
print (a)
b = input("Enter second word: ")
print (b)
try:
    print ("Mix-Up word is: " + "'" + b[0]+b[1]+a[2:] +" "+ a[0]+a[1]+b[2:] + "'")
except:
    print ("Word too short to mix up")'''

'''def mix_up(a, b):
     c = b[0:2]+ a[-1] + " " + a[0:2]+ b[2:]
     return c
 
print(mix_up("mi", "po"))'''
    
'''print ('first word')
word1 = input("> ")
print ("Second word")
word2 = input("> ")
def combine(word1, word2):
    if len(word1 and word2) >= 2:
        
        
        first_word = word1[0]

        first_word2 = word2[0]

        second_word = word1[1]

        second_word2 = word2[1]

        remaining_word = word1[2:]
    
        remaining_word2 = word2[2:]


        word2 = first_word + second_word + remaining_word
        
        word = first_word2 + second_word2 + remaining_word2
        
        return word1, word2
    
        
    
    elif len(word1 and word2) <= 2:
        return word1, word2
        combine(word1, word2)
print (combine(word1, word2))    
    

#def main():'''

import string
import operator
def most_common(word):
    diction = {}
    for char in word:
        diction[char] = word.count(char)
    sorted_dict = sorted(diction.items(), key=operator.itemgetter(1), reverse=True)
    keys = list(diction.keys())
    keys.sort()

    sorted_dict = dict(sorted_dict)
    limit = 0
    while len(sorted_dict) > 0:
        highest_count = 0
        highest_word = ""
        position = 0
        for x in range(len(keys)):
            if sorted_dict[keys[x]] > highest_count:
                highest_count = sorted_dict[keys[x]]
                highest_word = keys[x]
                position = x
        del sorted_dict[highest_word]
        del keys[position]
        print(highest_word+" %d" % highest_count)
        limit += 1
        if limit > 2:
            break

most_common(input("Enter a string\n"))
    
