#q8) Write a python menu driven program to show all queue operations performed on a list taken from the user
def isEmpty(qu):
    if qu == []:
        return True
    else:
        return False
def Enqueue(qu,item):
    qu.append(item)
    if len(qu) == 1:
        front = rear = 0
    else:
        rear = len(qu)-1
def Dequeue(qu):
    if isEmpty(qu):
        return "Underflow"
    else:
        item = qu.pop(0)
    if len(qu) == 0:
        front = rear = None
    return item
def Peek(qu):
    if isEmpty(qu):
        return "Underflow"
    else:
        front = 0
    return qu[front]
def Display(qu):
    if isEmpty(qu):
        print("Queue Empty !")
    elif len(qu) == 1:
        print(qu[0],"<== front,rear")
    else:
        front = 0
        rear = len(qu)-1
        print(qu[front],"<- front")
        for a in range(1,rear):
            print(qu[a])
        print(qu[rear],"<- rear")
queue = []
front = None
while True:
    print("QUEUE OPERATIONS")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch = int(input("enter the choice : "))
    if ch == 1:
        item = int(input("enter item :"))
        Enqueue(queue,item)
    elif ch == 2:
        item = Dequeue(queue)
        if item == "Underflow":
            print("Underflow ! Queue is empty !")
        else:
            print("Dequeue-ed item is",item)
    elif ch == 3:
        item = Peek(queue)
        if item == "Underflow":
            print("Queue is empty !")
        else:
            print("Frontmost item is",item)
        
    elif ch == 4:
        Display(queue)
    elif ch == 5:
        break
    else:
        print("Invalid choice !")
     
