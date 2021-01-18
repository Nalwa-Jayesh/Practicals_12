import random
l = []
n = 0
while n < 5:
    l.append(random.randint(1,99))
    n += 1
print(l)
size = len(l)
for i in range(size):
    for j in range(0,size-i-1):
        if l[j] == l[j+1]:
            break
for k in l :
    print(k)