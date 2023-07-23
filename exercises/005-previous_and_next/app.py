#Complete the function to return the previous and next number of a given numner.".
def previous_next(num):
  previous_number = num - 1
  next_number = num + 1
  return previous_number, next_number


#Invoke the function with any interger at its argument. 
print(previous_next(179))