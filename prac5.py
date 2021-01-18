#q5) WAP to recursively find the fiboniccai series upto n tems and take n from the user
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

nterms = int(input("Enter the number of terms :"))
print("Fibonacci Sequence :")
for i in range(nterms):
    print(fib(i))
