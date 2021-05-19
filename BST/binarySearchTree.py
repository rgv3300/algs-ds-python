class node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def lookupTree(rootNode,item):
    if rootNode == None:
        return
    if rootNode.data == item:
        return True
    if rootNode.data > item:
        return lookupTree(rootNode.left, item)
    else:
        return lookupTree(rootNode.right, item)

def insertNode(rootNode,item):
    temp = node(item)
    if rootNode == None:
        return
    elif rootNode.data > temp.data:
        if rootNode.left == None:
            rootNode.left = temp
            return
        insertNode(rootNode.left, item)
    else:
        if rootNode.right == None:
            rootNode.right = temp
            return
        insertNode(rootNode.right, item)

def searchMinimum(rootNode):
    min = rootNode
    if rootNode == None:
        return
    while min.left != None:
        min = min.left
    return min.data

def searchMaximum(rootNode):
    max = rootNode
    if rootNode == None:
        return
    while max.right != None:
        max = max.right
    return max.data


#must define rootNode first
a = node(3)
#automatically sort nodes after rootNode is inserted
insertNode(a,2)
insertNode(a,1)
insertNode(a,7)
insertNode(a,4)


b = lookupTree(a,8)
print(b)
