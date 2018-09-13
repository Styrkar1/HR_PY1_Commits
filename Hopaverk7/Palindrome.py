import re

def palindrome(x):
    back = x[::-1]
    back = back.lower()
    back = re.sub('!|,| |\'', '', back)

    newx = x
    newx = newx.lower()
    newx = re.sub('!|,| |\'', '', newx)

    if back == newx:
        print('"' + str(x) + '" is a palindrome.')
    elif back != newx:
        print('"' + str(x) + '" is not a palindrome.')


in_str = input("Enter a string: ")

palindrome(in_str)