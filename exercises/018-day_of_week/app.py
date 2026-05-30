# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):
  day = k%7
  real_day = [None,4,5,6,0,1,2,3]
  return real_day[k%7]


# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week(1))
