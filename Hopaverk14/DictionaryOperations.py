def menu_selection():
    print("Menu:")
    choice = input("add(a), remove(r), find(f): ")
    return choice

def execute_selection(ans):
    thelist = []
    if ans.lower() == "a":
        key = input("Key: ")
        val = input("value: ")
    elif ans.lower() == "r":
        thelist.remove(key)
        thelist.remove(val)
    return thelist

def dict_to_tuples(the_dict):
    dict_list = []
    for key, value in the_dict.items():
        temp = (key,value)
        dict_list.append(temp)
    return dict_list


# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()