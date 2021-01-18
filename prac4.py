#q4) WAP to recursively find the factorial of a natural number
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number :"))
print("Factorial of",n,"is",factorial(n))

