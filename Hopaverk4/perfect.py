n = int(input("Upper number for the range: ")) # Do not change this line

sum = 0
for i in range(1, n + 1):
    if(n % i == 0):
        sum = sum + i
if (sum == n):
    print(sum)
else:
    print("not it")