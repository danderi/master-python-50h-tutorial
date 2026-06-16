# Your code here
def divisible_binary(binary_string):
    binary_list = binary_string.split(",")
    
    result = []
    for binary in binary_list:
        # acá convertimos el binario a un entero base 2 usando la funcionalidad de int()
        decimal = int(binary, 2)
        
        if decimal % 5 == 0:
            result.append(binary)
            
    return ",".join(result)

print(divisible_binary("0100,0011,1010,1001"))