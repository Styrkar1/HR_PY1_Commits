def count_case(x):
    global lower
    global upper

    for i in list(x):
        if i.isupper():
            upper += 1

        elif i.islower():
            lower += 1

upper = 0
lower = 0
user_input = input("Enter a string: ")

count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)