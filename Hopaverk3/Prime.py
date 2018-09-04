n = int(input("Input a natural number: "))
if n > 1:
   for i in range(2,n):
       if (n % i) == 0:
           print("!Prime")
           break
   else:
       print("Prime")
else:
   print("!Prime")
