def safe_input(prompt,a_type):
    while True:
        try:
            x = input(prompt)

            if isinstance(x,float):
                print("Float")
                break
            elif isinstance(x,int):
                print("Int")
                break
            elif isinstance(x,str):
                print("String")
                break
            else:
                print("This program is retarded")
                break
        except ValueError:
            print("Error: please enter a value of ", a_type)
            continue


print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))
