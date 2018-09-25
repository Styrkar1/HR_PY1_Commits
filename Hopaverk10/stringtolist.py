import re
def to_list(x):
    x = re.split(',| ', x)
    return x

the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)