import string

sentence = input("Input a sentence: ")

unique_letters = []

for i in list(sentence):
    if i not in unique_letters:
        if i.isalpha():
            unique_letters.append(i)

print("Unique letters:", unique_letters)
