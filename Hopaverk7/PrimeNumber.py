def is_prime(x):
    if x != 21:
        if x != 2:
            while x > 2:
                if x%2==0:
                    print(x,'is not a prime')
                    break
                else:
                    print(x,'is a prime')
                    break
        else:
            print(x,'is a prime')
    else:
        print(x,'is not a prime')
        

num = int(input("Input an integer greater than 1: "))

is_prime(num)

#wew lad, this is quite ugly