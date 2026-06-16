# Your code here
def all_digits_even(numbers):
    even_num = []
    for i in numbers:
        if i >= 1000 and i <= 3000 and i%2 == 0:
            even_num.append(i)

    return ", ".join(str(i) for i in even_num)

print(all_digits_even([1000, 542, 1002, 3000, 4000, 2999, 2000]))