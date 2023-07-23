#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.

import math

def century(year):
  century_num = (year + 99) // 100
    
  return century_num



#Invoke the function with any given year. 
print(century(2001))