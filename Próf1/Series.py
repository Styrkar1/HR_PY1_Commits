initial = int(input("Initial value: "))
step = int(input("Step: "))
stepped = initial
total = 0
print(stepped)

while True:
    if total >= 100:
        break
    else:
        stepped = step + stepped
        total = stepped + total
        print(stepped)
print("Sum of series:",total + initial)

#the only way i know how to make something output like that is with a list, and we haven't even learned that.