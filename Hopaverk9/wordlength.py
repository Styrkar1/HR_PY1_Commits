with open('words.txt', 'r') as words:
    greatest = 0
    longest = ""
    for line in words:
        for word in line.split(" "):
            cnt = 0
            for t in list(word):
                cnt += 1
                if cnt > greatest:
                    greatest = cnt - 1
                    longest = word


print("Longest word is '" + str(longest.strip("\n")) + "' of length " + str(greatest))
