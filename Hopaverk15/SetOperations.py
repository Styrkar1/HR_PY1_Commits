def Menu():
    selected = input("1. Intersection\n2. Union\n3. Difference\n4. Quit\nSet operation: ")
    return selected

def intersection(numset,numset2):
    intersectionized = numset.intersection(numset2)
    answer = convertingtoint(intersectionized)
    return answer

def Union(numset,numset2):
    unionized = numset.union(numset2)
    answer = convertingtoint(unionized)
    return answer

def Difference(numset,numset2):
    Differenceed = numset.difference(numset2)
    answer = convertingtoint(Differenceed)
    return answer

def convertingtoint(types):
    listified = [int(x) for x in types]
    settified = set(listified)
    return settified

Numbers = input("Input a list of integers separated with a comma: ")
Numbers2 = input("Input a list of integers separated with a comma: ")

Num = Numbers.split(",")
numset = convertingtoint(Num)
Num2 = Numbers2.split(",")
numset2 = convertingtoint(Num2)
operation = "0"

print(numset)
print(numset2)
while operation != "4":
    operation = Menu()
    if operation == "1":
        print(intersection(numset,numset2))
    elif operation == "2":
        print(Union(numset,numset2))
    elif operation == "3":
        print(Difference(numset,numset2))
    else:
        operation == "4"