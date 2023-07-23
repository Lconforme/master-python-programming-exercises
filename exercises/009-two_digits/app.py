#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(num):
  tens = num // 10
  ones = num % 10
  return tens, ones

result = two_digits(45)
print(result)

