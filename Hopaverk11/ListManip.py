
def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

thelist = get_list()
print(thelist)
ans = input("Enter choice (m,r): ")

if ans.upper() == "M":
    mt = input("")
    modif = mt.split(",")
    mutate_list(thelist,int(modif[0]),int(modif[1]))

elif ans.upper() == "R":
    mv = int(input(""))
    remove_ch(thelist,mv)
print(thelist)