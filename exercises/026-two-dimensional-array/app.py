# Your code here
def two_dimensional_list(x,y):
    matrix_2 = []
    for i in range(x):
        aux = []
        for j in range(y):
            aux.append(i*j)
        matrix_2.append(aux)
    return matrix_2
        
print(two_dimensional_list(3,5))