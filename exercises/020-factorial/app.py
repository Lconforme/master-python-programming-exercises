# Your code here
def factorial(n):

    if n == 0:
        return 1
    
    return n * factorial(n - 1)

result = factorial(8)
print(result)
