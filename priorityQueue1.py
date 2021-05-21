#priority queue with arrays
def  priorityQueue:
    def __init__(self):
        self.queue = None
    
    def push(self,item):
        self.queue.append(item)
        self.queue.sort(reverse = True)

    def minElem(self):
        return self.queue[-1]

    def maxElem(self):
        return self.queue[0]

a = priorityQueue()

a.queue = []

a.push(5)
a.push(7)
a.push(10)
a.push(1)

print(a.minElem())
