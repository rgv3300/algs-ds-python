class Node:
    def __init__(self,data):
        self.data = None
        self.next = None

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
   
    def enqueue(self,data):
        newNode = Node(data)
        if self.tail == None:
             self.head= self.tail = newNode
             return
        self.tail.next = newNode
        self.tail = newNode

    def dequeue(self):
        if self.head == None and self.tail == None:
            print("Error: Empty list")
        temp = self.head
        self.head = temp.next
        del temp
        return self.head

a = queue()
a.enqueue(9)
a.enqueue(10)

print(a.head.data)
