def square(num):
    print(f"The square of number {num} is {num*num}\n")

def cube(num):
    print(f"The cube of number {num} is {num*num*num}\n")

def squareRoot(num):
    print(f"The square root of number {num} is {num ** 0.5}\n")

def cubeRoot(num):
    e = int(num ** (1/3))
    if num ** (1/3) == e + .99999:
        print(round(e,0))
    print(f"The cube root of number {num} is {num ** (1/3)}\n")

while(True):
    try:
        print('''****** Choose an Option ******
        1 . Square a number
        2 . Cube a number
        3 . Square root a number
        4 . Cube root a number
        5 . Exit the Program''')

        b = int(input("\nEnter Your Choice\n"))

        if b == 1:
            print("\nYou Choose for Squaring a Number\n")
            a = int(input("Enter Your Number\n"))
            square(a)
        elif b==2:
            print("\nYou Choose for Cubing a Number\n")
            a = int(input("Enter Your Number\n"))
            cube(a)
        elif b == 3:
            print("\nYou Choose for Squaroot a Number\n")
            a = int(input("Enter Your Number\n"))
            squareRoot(a)
        elif b==4:
            print("\nYou Choose for Cuberoot a Number\n")
            a = int(input("Enter Your Number\n"))
            cubeRoot(a)
        elif b==5:
            print("Thanks for Using This Program !!!")
            exit()
        else:
            print("Invalid Input !!\n Please Choose from 1 to 5")

    except Exception as e:
        print("Please Enter a Number not an Alphabet or a Special Character")

        

    