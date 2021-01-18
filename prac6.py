def sum_arr(arr,size):
    if size == 0:
        return 0
    else:
        return arr[size-1]+ sum_arr(arr,size-1)
n = int(input("Enter the size of list :"))
a= []
for i in range(n):
    ele = int(input("Enter the element : "))
    a.append(ele)
print("The list is :")
print(a)
print("Sum of list :")
b = sum_arr(a,n)
print(b)
