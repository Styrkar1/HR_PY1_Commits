secs_str = input("Input seconds: ") # do not change this line
time = int(secs_str)
hours = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print(hours,":",minutes,":",seconds) # do not change this line
