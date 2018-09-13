def find_min(x,y):
    global minimum
    if x < y:
        minimum = x
    elif y < x:
        minimum = y
    else:
        minimum = x

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
find_min(first,second)
print("Minimum: ", minimum)