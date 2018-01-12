'''
Created on Nov 30, 2016

@author: User
'''

def manipulate_data(data = []):
    #data = []
    solutions = []
    count_positives = 0
    sum_negatives = 0
    if data == []:
        return "[]"
    #elif len(data) > 2:
        #raise TypeError("takes only two argument " + str((len(data))) + " given")
    elif not isinstance(data, list):
        return "argument must be a list"
    for i in data:
        if not type(i) == int and float:
            raise ValueError("Only numeric numbers allowed")
        elif i < 0:
            sum_negatives += i
        elif i >= 0:
                count_positives += 1
    solutions.append(count_positives)
    solutions.append(sum_negatives)
    return solutions

#Binary converter 
def binary_converter(number):
  if number < 0:
    return "Invalid input"
  elif number == 0:
    return "0"
  elif number > 255:
    return "Invalid input"
  else:
    number = bin(number)
    number = number.lstrip('0b')
  return number

def main():
        print(manipulate_data([1,2,3,4,5,-4,-5,-10]))
        print(binary_converter(0))
        
if __name__== "__main__" : main()