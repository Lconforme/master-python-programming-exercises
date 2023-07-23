 #Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):
    last_digits = num % 100
    return last_digits

#Invoke the function with any interger greater than 9.
print(last_two_digits(1234))
