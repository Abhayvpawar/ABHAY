def createstack():
    STACK=[]
    return STACK

def push(STACK,item):
    STACK.append(item)


def pop(STACK):
    if len(STACK)==0:
        print("Stack is empty")
    else:
        return (STACK.pop())

def selectoption(ch):
    if ch==1:
        x=int(input("enter number to insert = "))
        push(STACK,x)
        print("pushed item= ",x)
        print(STACK)
    elif ch==2:
        X=pop(STACK)
        print("item popped = ",X)
        print(STACK)
    else:
        print("these are the elemnts of the stack= " ,STACK)


STACK=createstack()
ch=0
while(ch<=3):
    print("----stcak----")
    print("1 for push")
    print("2 for pop")
    print("3 for exit ")
    print("------------------")
    ch=int(input("Enter your choice = "))
    selectoption(ch)
