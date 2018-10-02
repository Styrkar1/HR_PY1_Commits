def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(thelist):
    thelist = list(map(int, thelist))
    total = 0
    for i in thelist:
        total = total + thelist[i]
    return total

a_list = get_list()
print(even_sum(a_list))
