# Q9. Write a program to reverse a stack.
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def isempty(self):
        return self.stack==[]
    def show(self):
        for element in reversed(self.stack):
            print(element)
def BottomInsert(s,element):
    if s.isempty():
        s.push(element)
    else:
        popped=s.pop()
        BottomInsert(s,element)
        s.push(popped)
def Reverse(s):
    if s.isempty():
        pass
    else:
        popped=s.pop()
        Reverse(s)
        BottomInsert(s,popped)
s=Stack()
s.push(50)
s.push(25)
s.push(14)
s.push(63)
s.push(34)
print("Original Stack")
s.show()
print("----------------------------")
print("\nRevese Stack")
Reverse(s)
s.show()
