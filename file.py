#part 1
'''f=open("first.txt","r")
print(f.read())
f.close()'''
#part 2
'''f=open("first.txt","r")
readinfo=f.readline()
print(readinfo)
f.close()'''
#part 3
'''f=open("first.txt","r")
readinfo=f.readlines()
print(readinfo)
f.close()'''
#part4
f=open("first.txt","r")
str1=" "
while str1:
    f.readline()
    print(str1,end=" ")
f.close()
