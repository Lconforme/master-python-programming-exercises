#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: You can resolve this exercise either importing the math module or without it 
def apple_sharing(n,k):
  apples_per_student = k // n
  remaining_apples = k % n

  return apples_per_student, remaining_apples
 
    

#Print the two answer per the example output.
print(apple_sharing(6,50))