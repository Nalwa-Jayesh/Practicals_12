#q10) WAP to open a file word.txt and count the number of "the's" in the file
file = open("word.txt","r")
lines = file.read().split()
count = 0
for i in lines :
    if i == 'the' or i == 'The':
        count += 1
print("the number of the's :",count)