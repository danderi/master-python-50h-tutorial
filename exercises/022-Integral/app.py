# Your code here
def squares_dictionary(num):
    aux = {}
    for i in range(1, num+1):
        aux[i]=i**2
    return aux

print(squares_dictionary(8))