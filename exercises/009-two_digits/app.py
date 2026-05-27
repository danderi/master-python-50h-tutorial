# Complete the function to return the tens digit and the units digit of any interger
def two_digits(number):
  # Your code here
    return int(str(number)[0]), int(str(number)[1])
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))
