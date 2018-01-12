'''
Created on Jan 9, 2017

@author: User
'''

text = str(input("Enter text: \n"))

def word_counter(text):
    # removes starting or trailing spaces also converts all to lower case.
    text = text.strip().lower() 
    
    #creates a new list with a diff variable
    text2 = text.split(' ')
    
    words = 0
    
    #create empty new list, the pop() function adds every removed element here 
    #excluding identical ones
    popped = []
    
    for i in text2:
        word = text2.pop() #removes the last element in a list
        
        #checks for identical words in the "text" and in the new list.
        if word in text2 and word not in popped:
            words += 1
            
        #Adds the popped element if it's not already in the the list    
        if not word in popped:
            popped.append(word)
            
    #return "Total number of words in your text is {}" .format(len(text.split(' '))) + ", " + str(words) + " word(s) appeared more than once" #for python 3.xx
    return "Total number of words in your text is %d" % len(text.split(' ')) + ", " + str(words) + " word(s) appeared more than once." #for python 2.xx and 3.xx

#Opens specified file or creates new one if file doesn't exists
file = open("textfile.txt", "w+")

file.write(text) #write  to file

file.close()

file = open("textfile.txt", "r")#open file in read mode
if file.mode == "r":#check to make sure file was opened in read mode
    contents = file.read()#read every content of the file
    print(word_counter(contents))





def main():
    #print(word_counter(text))
    pass
    
    
    
if __name__ == "__main__": main()