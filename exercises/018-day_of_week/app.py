#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(K):
  day_of_week_num = (K + 3) % 7

  return day_of_week_num



#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(1))