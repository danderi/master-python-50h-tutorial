# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  aux = str(num)
  number = 0
  for i in aux:
    number += int(i)

  return number


# Invoke the function with any three-digit number
print(digits_sum(123))
