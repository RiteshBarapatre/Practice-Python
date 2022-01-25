import string
import random
# s1 = string.ascii_letters #This is a function of string which contain
# All alphabet in both lower and upper case

s1 = string.ascii_lowercase #Contain lowercase alphabet
# print(s1)

s2 = string.ascii_uppercase #Contain uppercase alpphabet
# print(s2)

s3 = string.digits #Contain number from 0 to 9
# print(s3)

s4 = string.punctuation #Contains all punctuations
# print(s3)
while(True):
    try:
        a = int(input("Enter the length of a password: \n"))
        break
    except ValueError as e:
        print("Enter a number not a letter")
        
s = [] #We create a empty list
#This is extend is same as append but we append the list in another list
#And in extend we add element of list to another list
s.extend(list(s1)) 
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# print(s)
random.shuffle(s)
# print(s)
print("Your password is :")
print("".join(s[0:a])) #If we didn't write .join then it will return list