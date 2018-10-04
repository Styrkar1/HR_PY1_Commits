def merge_lists(list1,list2):
    uniq_list = []
    list3 = list1 + list2
    for i in list3:
        if not i in uniq_list:
            uniq_list.append(i)
    #apperantly the output isn't supposed to be INT
    #uniq_list = list(map(int, uniq_list))
    uniq_list.sort()
    return uniq_list

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
