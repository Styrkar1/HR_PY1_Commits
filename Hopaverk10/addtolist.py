def triple_list(x):
    x = []
    y = []
    z = []
    a = []
    newchar = ""
    while newchar.upper() != "EXIT":
        newchar = input("Enter value to be added to list: ")
        x.append(newchar)
        y.append(newchar)
        z.append(newchar)
        a.extend(x)
        a.extend(y)
        a.extend(z)
    return a



initial_list = []
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
