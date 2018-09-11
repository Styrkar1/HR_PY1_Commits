s = input("Input a string: ")

ls = list(s)

store = ""
for i in ls:
    if i.isdigit():
        store = store + i
print(store)