'''
Created on Nov 28, 2016

@author: User
'''
def calculate_tax(people):
    people = dict(people)
    if people == {}:
        return '{}'
    for i in people:
        if type(people[i]) == str:
            raise ValueError ("Only numeric Values needed")
    else:
        for k in people:
            if people[k] < 1000:
                people[k] = 0
                               
            elif people[k] >= 50000:
                firstTax = 1000 * 0.0
                secondTax = 9000 * 0.1
                thirdTax = 10200 * 0.15
                fourthTax = 10550 * 0.2
                fifthTax = 19250 * 0.25
                sixthTax = (people[k] - 50000) * 0.3
                people[k] = (firstTax + secondTax  + thirdTax+ fourthTax + fifthTax 
                             + sixthTax)
                
            elif people[k] >= 30750:
                firstTax = 1000 * 0.0
                secondTax = 9000 * 0.1
                thirdTax = 10200 * 0.15
                fourthTax = 10550 * 0.2
                fifthTax = (people[k] - 30750) * 0.25
                people[k] = (firstTax + secondTax  + thirdTax+ fourthTax
                              + fifthTax)
                                             
            elif people[k] >= 20200:
                firstTax = 1000 * 0.0
                secondTax = 9000 * 0.1
                thirdTax = 10200 * 0.15
                fourthTax = (people[k] - 20200) * 0.2
                people[k] = (firstTax + secondTax  + thirdTax+ fourthTax)
                 
            elif people[k] >= 10000:
                firstTax = 1000 * 0.0
                secondTax = 9000 * 0.1
                thirdTax = (people[k] - 10000) * 0.15
                people[k] = (firstTax + secondTax  + thirdTax)
                    
            elif people[k] >= 1000:
                firstTax = 1000 * 0.0
                secondTax = (people[k] - 1000) * 0.1
                people[k] = (firstTax + secondTax)
              
        return people
        
        
        """
            New idea declare from first to sixth tax as variable with their
            solution ready to be used. then inside the if else statements you can
            just add them for each individual and only have to calculate the last 
            tax of the total income minus the highest tax level
        """
        
def main():
        print(calculate_tax({'James': 500, 'John' : 20500, 'Mary' : 70000}))
        
if __name__== "__main__" : main()
             
                
                