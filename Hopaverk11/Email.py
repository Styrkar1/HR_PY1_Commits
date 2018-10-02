
def get_emails():
    listing = []
    while True:
        inp = input("Email address: ")
        if inp.upper() == "Q":
            break
        else:
            listing.append(inp)
    return listing

def get_names_and_domains(emails):
    newlist = []
    for i in emails:
        newlist.append(i.split('@'))
    newlist = tuple(newlist)
    
    return newlist


email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)