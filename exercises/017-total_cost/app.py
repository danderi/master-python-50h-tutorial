# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    cents = c * n
    dollars = d * n
    if cents > 99:
        dollars += round(cents / 100)
        cents = cents % 100

    return dollars, cents


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
