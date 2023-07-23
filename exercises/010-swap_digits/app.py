#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  tens_num = num // 10
  ones_num = num % 10
  swapped_num = ones_num * 10 + tens_num
  return swapped_num
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
