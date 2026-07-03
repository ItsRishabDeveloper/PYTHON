if True:
    print("This is true")
else:
    print("This is false") 
a = int(input("Enter a number: "))
if a > 0:
    if a % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
elif a < 0:
    print("The number is negative")