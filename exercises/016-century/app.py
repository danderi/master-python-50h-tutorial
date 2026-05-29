# Complete the function to return the respective number of the century
import math
def century(year):
  aux = 0
  aux2 = year%100
  if aux2 > 0:
    aux = 1
  return round(year/100)+aux


# Invoke the function with any given year
print(century(2001))
