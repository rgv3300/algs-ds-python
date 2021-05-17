class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.data = None
    def push(self,item):
        if self.data == None:
            self.data = Node(item)
        else:
            new = Node(item)
            new.next = self.data
            self.data = new
    def pop(self):
        popped = self.data
        self.data = self.data.next
        popped.next = None
        return popped.data

a = Stack()
a.push(5)
print(a.data.data)
a.push(6)
print(a.data.next.data)
a.push(7)
print(a.data.next.data)
a.pop()
