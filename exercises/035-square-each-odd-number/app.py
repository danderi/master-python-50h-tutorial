# Your code here
def square_odd_numbers(str_num):
    aux = []
    for i in str_num:
        if i == ",":
            continue
        elif int(i)%2 != 0:
            aux.append(int(i)**2)
    return aux

print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))