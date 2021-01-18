a=eval(input("Enter the tuple :"))
b=0
for i in range(0,len(a)):
    b+=a[i]
print("Average :",b/len(a))