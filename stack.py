class Node:
    def _init_(self, data, next):
        self.data = None
        self.next = None

class Stack:
    def _init_(self):
        self.head = None
    def push(self,item):
        if self.head == None:
            self.head = Node(item)
        else:
            new = Node(item)
            new.next = self.head
            self.head = new
    def pop(self):
        popped = self.head
        self.head = self.head.next
        popped.next = None
        return popped.data

a = Stack()
a.push(5)
print(a)
a.push(6)
a.push(7)
print(a)
a.pop()
