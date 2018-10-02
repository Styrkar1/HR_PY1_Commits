def sort_list(a_list):
    a_list = a_list.sort()
    

def main():
    number = "0"
    a_list = []

    while number.isdigit():
        number = input()
        if number.isdigit():
            a_list.append(number)
        else:
            break
    
    a_list = [int(x) for x in a_list]
    
    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()