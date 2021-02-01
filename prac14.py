l = eval(input("Enter the list in ascending order :"))
beg = 0
end = len(l)-1
item = int(input("Enter the item :"))
while beg <= end:
    mid = (beg+end)//2
    if item == l[mid]:
        print("found")
        break
    elif item > l[mid]:
        beg = mid + 1
    else :
        end = mid - 1