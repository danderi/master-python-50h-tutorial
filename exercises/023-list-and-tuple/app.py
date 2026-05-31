# Your code here
def list_and_tuple(*args):
    num_list = list(args)
    str_list = [str(i) for i in (num_list)]
    tpl = tuple(str_list)
    return (str_list),(tpl)
    

lista , tupla = list_and_tuple(34,67,55,33,12,98)
print(lista)
print(tupla)