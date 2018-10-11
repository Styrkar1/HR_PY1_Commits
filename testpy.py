def my_func(a_dict):
   for key, val in a_dict.items():
       if key[0] == 'n':
           a_dict[key] = val*3

my_dict = {'ps4': 2, 'nintendo': 4, 'todo': 1}
my_func(my_dict)
print(my_dict)