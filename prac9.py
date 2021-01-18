#q9) WAP to open a file 'practical.txt' and count the number of lines starting with T or t
file = open("practical.txt","r")
lines = file.read().split('\n')
count = 0
for i in lines :
    if i[0] == 't' or i[0] == 'T':
        count += 1
print("the number of t's :",count)
