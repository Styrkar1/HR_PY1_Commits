words = ""
while words != ".ay":
    words = input(str("Enter a word: "))
    words = words.split(' ')
    for i in words:
        i = i + '%say' % (i[0]) 
        i = i[1:]
        print (i)