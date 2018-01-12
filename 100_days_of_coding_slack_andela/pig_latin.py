'''
Created on Jan 9, 2017

@author: User
'''
text = str(input("Enter a word: "))
text = text.strip()

def pig_latin(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(text) <= 0:
        return "Invalid Input, please enter a Word"
    elif len(text.split()) > 1:
        return "Invalid Input, Not more than one word is allowed"
    text = list(text)
    if text[0] in vowels:
        text.append("yay")
    elif text[0] not in vowels and text[1] not in vowels:
        cons = text.pop(0)#removes the first consonant
        cons2 = text.pop(0)#removes the second consonant which has now become the first
        text.append(cons)
        text.append(cons2)
        text.append("ay")
    elif text[0] not in vowels:
            cons = text.pop(0)
            text.append(cons)
            text.append("ay")
        

    return''.join(text)

print(pig_latin(text))
        
    