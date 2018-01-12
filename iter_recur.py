'''
Created on Nov 30, 2016

@author: User
'''

def replicate_iter(times, data):
  result = []
  if times <= 0:
    return []
  elif type(times) != int:
    raise ValueError("Invalid argument")
  elif type(data) != int and type(data) != str:
    raise ValueError("Invalid argument")
  else:
    for i in range(times):
      result.append(data)
  return result
  
def replicate_recur(times, data):
  result = []
  if times <= 0:
    return []
  elif type(times) != int:
    raise ValueError("Invalid argument")
  elif type(data) != int and type(data) != str:
    raise ValueError("Invalid argument")
  else:
    return [data] * times
        
      
    #return result   
      
def main():
        print(replicate_iter(3, 'z'))
        print(replicate_recur(3, '5'))
        
if __name__== "__main__" : main()