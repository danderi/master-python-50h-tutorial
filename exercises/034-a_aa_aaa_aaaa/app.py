def computed_value(a):
    total = 0
    for i in range(1, 5):
        total += int(str(a) * i)
    return total

print (computed_value(9))  