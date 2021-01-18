#q1) WAP to determine how many times a given letter occurs in a string
count = 0
s = input("Enter a string : ")
l = input("Enter the letter to be found : ")
for i in s:
    if i == l:
        count+=1
print(f"{l} came {count} times in '{s}'")