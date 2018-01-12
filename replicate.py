'''
Created on Jan 10, 2017

@author: User
'''
def replicate_iter(times, data):
  if times <= 0:
    return []
  elif type(times) != int:
      raise ValueError("invalid input")
  elif type(data) != int and type(data) != str:
    raise ValueError("invalid input")
  else:
    return [data for x in range(times)]

def replicate_recur(times, data):
    print("Times called with", times)
    if times <= 0:
      return []
    elif type(times) != int:
      raise ValueError("invalid input")
    elif type(data) != int and type(data) != str:
      raise ValueError("invalid input")
    else:
      result = []
      result =  replicate_recur(times-1, data)
      result.append(data)
      #print(result)
    return result


def main():
    print(replicate_iter(3, 5))
    print(replicate_recur(3, 5))
    