def is_float(x):
    if isinstance(x ,float):
        print("True")
    else:
        print("False")

print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))