#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  hundreds_digit = num // 100
  tens_digit = (num // 10) % 10
  ones_digit = num % 10
  
  digit_sum = hundreds_digit + tens_digit + ones_digit
  return digit_sum


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))