# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  if num > 9:
   return int(str(num)[-2])


# Invoke the function with any integer
print(tens_digit(568))
