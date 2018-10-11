def make_sublists(a_list):
    the_sub = []
    number = 0
    newnum = 1
    for i in a_list:
        number += 1

    for i in range(0, (number*2)):
        if i < number:
            the_sub.append(a_list[:i])
        elif i == number:
            the_sub.append(a_list)
            the_sub.append(a_list[1:-newnum])
        elif i > number: 
            the_sub.append(a_list[newnum:])
            newnum += 1
    return the_sub

inp = input("Enter a list separated with commas: " )

thelist = inp.split(",")

print(make_sublists(thelist))

