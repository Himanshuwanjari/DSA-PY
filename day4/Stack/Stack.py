import sys
class Stack:
    def __init__(self):
        self.myStack=[]
    
    def push(self,value):
        self.myStack.append(value)
        print('Element is pushed')

    def display(self):
        print(self.myStack)
    
    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            self.myStack.pop()
            print('Element is poped')

    def peek(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            # print(self.myStack[-1])
            print('Peek element is ',self.myStack[len(self.myStack)-1])

    def deleteStack(self):
        self.myStack = None

    
obj=Stack()
print('Stack has created.')
while True:
    print('1. Push Operation')
    print('2. Display Stack')
    print('3. Pop Stack')
    print('4. Peek Element')
    print('5. Delete Stack')
    print('7. Exit')
    choice = int(input('Enter Your choice: '))
    if choice == 1:
        value = int(input('Enter value to push in stack: '))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
            obj.pop()
    elif choice == 4:
            obj.peek()
    elif choice == 5:
            obj.deleteStack()
    else :
        sys.exit()