# Your code here
import string

def letters_and_digits(frase):
    elem = {"DIGITS": 0, "LETTERS" : 0}
    for i in frase:
        if i.isdigit():
            elem["DIGITS"]+=1
        elif i.isalpha():
            elem["LETTERS"] += 1
        
    return f"LETTERS {elem['LETTERS']} DIGITS {elem['DIGITS']}"

print(letters_and_digits("hello world! 123"))