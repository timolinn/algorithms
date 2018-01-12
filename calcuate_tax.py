'''
Created on Nov 28, 2016

@author: User
'''
def calculate_tax(inc = dict()):
  #inc = dict(inc)
  if inc == {}:
    return {}
  
  for i in inc.keys():
    if type(inc[i]) != int and type(inc[i]) != float:
        raise ValueError ("Only numeric Values needed")
  try:
    for i in inc.keys():
      if inc[i] <= 1000:
        inc[i] = 0
      elif inc[i] <= 10000:
        inc[i] = (inc[i] - 1000) * 0.1
      elif inc[i] <= 20200:
        inc[i] = (inc[i] - 10000) * 0.15 + 900
      elif inc[i] <= 30750:
        inc[i] = (inc[i] - 20200) * 0.2 + 2430
      elif inc[i] <= 50000:
        inc[i] = (inc[i] - 30750) * 0.25 + 4540
      else:
        inc[i] = (inc[i] - 50000) *0.3 + 9352.5
    return inc
  except (AttributeError) as e:
    return ("Non-numeric values not allowed: ({})".format(e))

def tax_calculation(people = {}):
  if people == {}:
    return {}
  try:
    people == isinstance(people, dict)
    return 'True'
  except Exception:
    return "The provided input is not a dictionary"
  for i, people[i] in people.items():
    if not isinstance(people[i], (int,float)):
      return "Allows only numeric values for income"
    elif people[i] <= 1000:
        people[i] = 0
    elif people[i] <= 10000:
        people[i] = (people[i] - 1000) * 0.1
    elif people[i] <= 20200:
        people[i] = (900 + ((people[i]-10000)*0.15))
    elif people[i] <= 30750:
        people[i] = (2430 + ((people[i]-20200)*0.2))
    elif people[i] <= 50000:
        people[i] = (4540 + ((people[i]-30750)*0.25))
    elif people[i] > 50000:
        people[i] = (9352.5 + ((people[i] - 50000)*0.3))
  return people 


def main():
        print(calculate_tax({'James': 500, 'John' : 20500, 'Mary' : 70000}))
        print(tax_calculation({'James': 500, 'John' : 20500, 'Mary' : 70000}))
        print(tax_calculation({}))
        
if __name__== "__main__" : main()

def calculate_tax(people):
        while True:
            try:
                iterating_people = people.keys()
                for key in iterating_people:
                    earning = people[key]
                    if earning <= 1000:
                        people[key] = 0 
                    elif earning in range(1001,10001):
                        tax1 = 0 * 1000
                        tax2 = 0.1 * (earning - 1000)
                        total_tax = tax1 + tax2
                        people[key] = total_tax
                    elif earning in range(10001,20201):
                        tax1 = 0 * 1000
                        tax2 = 0.1 *9000
                        tax3 = 0.15 * (earning - 10000)
                        total_tax = tax1+tax2+tax3
                        people[key] = total_tax
                    elif earning in range(20201,30751):
                        tax1 = 0 * 1000
                        tax2 = 0.1 * 9000
                        tax3 = 0.15 * 10200
                        tax4 = 0.20 * (earning - 20200)
                        total_tax = tax1+tax2+tax3+tax4
                        people[key] = total_tax
                    elif earning in range(30751,50001):
                        tax1 = 0 * 1000
                        tax2 = 0.1 * 9000
                        tax3 = 0.15 * 10200
                        tax4 = 0.20 * 10550
                        tax5 = 0.25 * (earning - 30750)
                        total_tax = tax1+tax2+tax3+tax4+tax5
                        people[key] = total_tax
                    elif earning > 50000:
                        tax1 = 0 * 1000
                        tax2 = 0.1 * 9000
                        tax3 = 0.15 * 10200
                        tax4 = 0.20 * 10550
                        tax5 = 0.25 * 19250
                        tax6 = 0.3 * (earning - 50000)
                        total_tax = tax1+tax2+tax3+tax4+tax5+tax6
                        people[key] = total_tax
                return people
                break
            except (AttributeError,TypeError):
                raise ValueError('The provided input is not a dictionary')
