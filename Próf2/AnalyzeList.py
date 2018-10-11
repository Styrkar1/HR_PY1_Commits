def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

#a short function to sort lists
def sort_list(a_list):
    a_list = a_list.sort()
    
number = "0"
a_list = []

while number.isdigit():
    number = input("Enter integers separated with commas: ")
    for i in number.split(","):
        if i.isdigit():
            a_list.append(i)
        else:
            print("Incorrect input!")
            break

#converting the list into numbers
a_list = [int(x) for x in a_list]
p_list = []

#finding the prime numbers in the list
for i in a_list:
    if is_prime(i) == True:
        if i not in p_list:
            p_list.append(i)

#finding the minimum number
min = 1000
for i in a_list:
    if i < min:
        min = i

#finding the maximum number
max = 0
for i in a_list:
    if i > max:
        max = i

#calculating the average number
count = 0
sum = 0
for i in a_list:
    count += 1
    sum += i
avg = sum / count
#this makes it so there are always two decimal places
avg = "%.2f" % avg

#the result is printed in this disgusting way because when i put the words along with the lists i got problems and this was the quick fix
print("Input list: ", end='')
print(a_list)
#using a function to sort the list
sort_list(a_list)
print("Sorted list:  ", end='')
#printing the sorted list
print(a_list)

#sorting the prime list
sort_list(p_list)
print("Prime list:  ", end='')
print(p_list)
#printing the min, max and average
print("Min: " + str(min) + ", Max: " + str(max) + ", Average: " + str(avg))