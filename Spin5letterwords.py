'''
Created on Nov 24, 2016

@author: User
'''


def spinWords(sentence):
    sent = sentence.split(' ')
    for i in range(0, len(sent)):
        if len(sent[i]) >= 5:
            sent[i] = list(sent[i])
            sent[i].reverse()
            sent[i] = ''.join(sent[i])
    sent = ' '.join(sent)
    return sent
    
    
def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string

def main():
    print(spinWords('My name is Mex, how may i help you mr clattenburg. He knows he is always welcome here'))
    print(spin_words('My name is Mex, how may i help you mr clattenburg. He knows he is always welcome here'))    
    
    
if __name__ == "__main__": main()