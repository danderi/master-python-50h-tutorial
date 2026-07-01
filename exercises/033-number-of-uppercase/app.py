# Your code here
def number_of_uppercase(sentence):
    elem = {"UPPERCASE":0, "LOWERCASE":0}
    for i in sentence:
        if i.islower():
            elem["LOWERCASE"]+=1
        elif i.isupper():
            elem["UPPERCASE"]+=1

    return f'UPPERCASE : {elem["UPPERCASE"]}\nLOWERCASE: {elem["LOWERCASE"]}'

print(number_of_uppercase("Hello world!"))