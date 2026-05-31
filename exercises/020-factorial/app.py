# Your code here
def factorial(num):
    aux = 1
    for i in range(num+1):
        if i == 0:
            continue
        else:
            aux*=i
    return aux

print(factorial(8))