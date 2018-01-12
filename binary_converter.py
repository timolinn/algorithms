def binary_converter(number):
    if number < 0 or number > 255:
        return "Invalid input"
    if number == 0:
        return '0'
    else:
        bits = [32, 16, 8, 4, 2, 1]
        result = []
        for i in bits:
            if number // i:
                number -= i
                result.append('1')
            else:
                result.append('0')
        #return result
        res = ''.join(result)
        return (res)
def binary_convertr(number):
  InvalidInput = "Invalid input"  
  if number < 0 or number > 255:
    return InvalidInput
  if number == 0:
    return '0'
  else:
    bits = [32, 16, 8, 4, 2, 1]
    result = []
    for i in bits:
      if number // i:
        number -= i
        result.append('1')
      else:
        result.append('0')
    result = ''.join(result)
    return str(int(result))


def binary_convert(number):
  InvalidInput = "Invalid input"
  if number < 0 or number > 255:
    return InvalidInput
  if number == 0:
    return '0'
  else:
    result = bin(number)
    result = result.lstrip('0b')
    return result

def main():
    print(binary_convert(-62))
    print(binary_converter(62))
    
    
if __name__ =="__main__":
    main()