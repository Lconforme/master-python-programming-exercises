#Complete the function to return the amount of days it will take to cover a route.
#HINT: You may need to import the math module for this exercise.

import math

def car_route(N, M):
    days_needed = (M + N - 1) // N
    return days_needed


#Invoke the function with two intergers.
print(car_route(20,40))