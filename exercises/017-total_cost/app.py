#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    total_cents = (d * 100 + c) * n

    total_dollars = total_cents // 100
    total_cents %= 100

    return (total_dollars, total_cents)
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(15, 22, 4))
