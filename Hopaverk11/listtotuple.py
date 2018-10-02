def list_to_tuple(a_list):
    ret = ()
    for i in a_list:
        if i.isdecimal():
            ret = ret + (int(i),)
        else:
            ret = "Error. Please enter only integers.\n()"
            return ret

    return ret

a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)