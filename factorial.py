#Calculate the factorial of a given number 
#Find the number of trailing zeros in that factorial
#It means tell how many zero are in the end of the number 

def factorial(n):
    if n == 1 or n==0:
        return 1
    return n * factorial(n-1)

def factorialTrailingZero(number):
    fac = factorial(number)
    print(fac)
    count = 0
    while(fac%10 == 0):
        count = count + 1
        fac = fac/10
    return count

a = int(input("Enter The Number :\n"))
b = factorial (a)
print(f"The Factorial of {a} is {b}")

