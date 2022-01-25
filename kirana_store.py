#Write a python program which will keep adding a stream of numbers inputted by the user.
#the adding stops as soon as the user presses the q key on the keyboard

sum = 0
while(True):
    a = input("\nEnter the price or press q to quit :\n")
    if a!= 'q':
        sum = sum + int(a)
        print(f"\nTotal till now = {sum}")
       
    else:
        print("\nYour Grand Total = ",sum)
        print("\nThanks for shopping with us !!")
        break
