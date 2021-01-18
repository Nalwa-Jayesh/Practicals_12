#q3) WAP to take the first number (a) ,common difference (d) and number of terms (n) from the user and display the arithmatic progression
a = int(input("Enter the first number : "))
d = int(input("Enter the common difference : "))
n = int(input("Enter the number of terms : "))
for i in range(1,n+1):
    print(f"{a}",end=' ')
    a+=d