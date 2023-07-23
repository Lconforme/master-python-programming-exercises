#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
  num_str = str(num)
  decimal_pos = num_str.find('.')
  first_digit = int(num_str[decimal_pos + 1])
    
  return first_digit



#Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.79))