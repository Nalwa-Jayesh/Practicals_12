#q7) Write a python menu driven program to show all stack operations performed on a list taken from the user
def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top = len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk)-1
        return item
def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk)-1
        return stk[top]
def Display(stk):
    if isEmpty(stk):
        print("Stack is empty")
    else:
        top = len(stk)-1
        print(stk[top],"<- top")
        for a in range(top-1,-1,-1):
            print(stk[a])
stack = []
top = None

while True:
    print("STACK OPERATIONS")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch = int(input("Enter the choice (1-5) :"))
    if ch == 1:
        item = int(input("Enter the item :"))
        Push(stack,item)
    elif ch == 2:
        item = Pop(stack)
        if item == "Underflow":
            print("Underflow ! Stack is empty !")
        else:
            print("Popped item is",item)
    elif ch == 3:
        item = Peek(stack)
        if item == "Underflow":
            print("Underflow ! Stack is empty !")
        else:
            print("Topmost item is",item)
    elif ch == 4:
        Display(stack)
    elif ch == 5:
        break
    else:
        print("Invalid Choice !!!!")