'''
Created on Nov 24, 2016

@author: User
'''


# shuffle = lambda st: " ".join(x[::-1] for x in st.split())
#
# 'shuffle()' does the same as 'reverse_word_chars()' below

def reverse_words(s):
    """returns string that is just like s except that the word order is
    reversed."""
    return ' '.join(reversed(s.split()))

def reverse_chars(s):
    """returns string whose char order is mirror image of s """
    return ''.join(reversed(s))

def reverse_word_chars(s):
    """returns string that is just like s except that the letters in each word
    are reversed"""
    return ' '.join(reversed(x) for x in s.split())

def shuffle(st):
    st = st.split(' ')
    for x in range(0, len(st)):
        st[x] = list(st[x])
        st[x].reverse()
        st[x] = ''.join(st[x])
    st = ' '.join(st)
    return st


def main():
    print(shuffle('My name is Mex'))
    print(reverse_words("My name is Mex"))
    
if __name__ == "__main__": main()