a = 2
b = 4

if a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")

if a < b and a != 0:
    print("a is less than b and not equal to 0")

if a > b or b != 0:
    print("Either a is greater than b or b is not equal to 0")

if a > 0:
    if b > 0:
        print("Both a and b are positive")

if a == 0:
    pass 
else:
    print("a is not zero")
