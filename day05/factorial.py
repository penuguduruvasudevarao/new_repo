n =int(input("Enter a number: "))
def facto(n):
    if n==0 or n==1: 
        return 1 
    else:
        return n*facto(n-1)


if n<0:
    print("Factorial of negative number is not possible")
else:
    print("Factorial of", n, "is", facto(n))