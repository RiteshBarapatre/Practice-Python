print("\n***** Welcome To Ritesh's Trignometric Calculator *****\n")
def Sin():
    num = int(input("Enter The value of theeta in degree !!!\n"))
    if num == 0:
        print("sin 0° = 0")
    elif num == 30:
        print("sin 30° = 1/2")
    elif num == 45:
        print("sin 45° = 1/√2")
    elif num == 60:
        print("sin 60° = √3/2")
    elif num == 90:
        print("sin 90° = 1")
    else:
        print("Invalid Input !!!")
        print("Please Enter the valid input")
        print("like : 0,30,45,60,90")

def Cos():
    num = int(input("Enter The value of theeta in degree !!!\n"))
    if num == 0:
        print("cos 0° = 1")
    elif num == 30:
        print("cos 30° = √3/2")
    elif num == 45:
        print("cos 45° = 1/√2")
    elif num == 60:
        print("cos 60° = 1/2")
    elif num == 90:
        print("cos 90° = 0")
    else:
        print("Invalid Input !!!")
        print("Please Enter the valid input")
        print("like : 0,30,45,60,90")


def Tan():
    num = int(input("Enter The value of theeta in degree !!!\n"))
    if num == 0:
        print("tan 0° = 0")
    elif num == 30:
        print("tan 30° = 1/√3")
    elif num == 45:
        print("tan 45° = 1")
    elif num == 60:
        print("tan 60° = √3")
    elif num == 90:
        print("tan 90° = Infinite/Not Defined")
    else:
        print("Invalid Input !!!")
        print("Please Enter the valid input")
        print("like : 0,30,45,60,90")

def Cot():
    num = int(input("Enter The value of theeta in degree !!!\n"))
    if num == 0:
        print("cot 0° = Infinite/Not Defined")
    elif num == 30:
        print("cot 30° = √3")
    elif num == 45:
        print("cot 45° = 1")
    elif num == 60:
        print("cot 60° = √3/3")
    elif num == 90:
        print("cot 90° = 0")
    else:
        print("Invalid Input !!!")
        print("Please Enter the valid input")
        print("like : 0,30,45,60,90")

def Cosec():
    num = int(input("Enter The value of theeta in degree !!!\n"))
    if num == 0:
        print("cosec 0° = Infinite/Not Defined")
    elif num == 30:
        print("cosec 30° = 2")
    elif num == 45:
        print("cosec 45° = √2")
    elif num == 60:
        print("cosec 60° = 2√3/3")
    elif num == 90:
        print("cosec 90° = 1")
    else:
        print("Invalid Input !!!")
        print("Please Enter the valid input")
        print("like : 0,30,45,60,90")

def Sec():
    num = int(input("Enter The value of theeta in degree !!!\n"))
    if num == 0:
        print("sec 0° = 1")
    elif num == 30:
        print("sec 30° = 2√3/3")
    elif num == 45:
        print("sec 45° = √2")
    elif num == 60:
        print("sec 60° = 2")
    elif num == 90:
        print("sec 90° = Infinte/Not Defined")
    else:
        print("Invalid Input !!!")
        print("Please Enter the valid input")
        print("like : 0,30,45,60,90")

while(True):
    b = '''\nPlease ! Choose an option from the following.... 
    1 . sin
    2 . cos
    3 . tan
    4 . cot
    5 . sec
    6 . cosec
    7 . Exit'''
    print(b)
    a = int(input("\nEnter Your Choice !!!\n"))
    if a == 1:
        print("\nYou choose for sin....\n")
        Sin()
    elif a == 2:
        print("\nYou choose for cos....\n")
        Cos()
    elif a == 3:
        print("\nYou choose for tan....\n")
        Tan()
    elif a == 4:
        print("\nYou choose for cot....\n")
        Cot()
    elif a == 5:
        print("\nYou choose for sec....\n")
        Sec()
    elif a == 6:
       print("\nYou choose for cosec....\n")
       Cosec()
    elif a == 7:
        exit()
    else:
        print("Invalid Input !!!")
        print("Please Enter Number from 1 to 6")

