class node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
       	self.right = None
        self.parent = None

def lookupTree(rootNode,item):
    if rootNode == None:
        return
    if rootNode.data == item:
        return rootNode
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
           temp.parent = rootNode
           rootNode.left = temp
           return
        insertNode(rootNode.left, item)
    else:
        if rootNode.right == None:
            temp.parent = rootNode
            rootNode.right = temp
            return
        insertNode(rootNode.right, item)

def searchMinimum(rootNode):
    min = rootNode
    if rootNode == None:
        return
    while min.left != None:
        min = min.left
    return min

def searchMaximum(rootNode):
    max = rootNode
    if rootNode == None:
        return
    while max.right != None:
        max = max.right
    return max

def deleteNode(rootNode,item):
    temp = lookupTree(rootNode,item)
    if rootNode == None:
        return
    if temp.left is None and temp.right is None:
        temp.parent.left = None
        temp.parent.right = None
    if temp.data < temp.parent.data:
        if temp.left is not None and temp.right is None:
            temp.parent.left = temp.left
        elif temp.left is None and temp.right is not None:
            temp.parent.left = temp.right
        else:
            inorderSucc =  inOrder(temp)
            temp1 = inorderSucc
            temp.parent.left = temp1
            temp1.right = temp.right
            temp1.left = temp.left
            del inorderSucc
    if temp.data > temp.parent.data:
        if temp.left is not None and temp.right is None:
            temp.parent.right = temp.left
        elif temp.left is None and temp.right is not None:
            temp.parent.right = temp.right
        else:
            inorderSucc = inOrder(temp)
            temp1 = inorderSucc
            temp.parent.right = temp1
            temp1.right = temp.right
            temp1.left = temp.left
            del inorderSucc
def inOrder(root):
    if root.right != None:
        root = root.right
        while root.left:
            root = root.left
        return root
    else:
        parent = root.parent
        while parent != None:
            if parent.left == root:
                break
            root = parent
            parent = root.parent
        return parent


    

#must define rootNode first
a = node(10)
#automatically sort nodes after rootNode is inserted
insertNode(a,6)
b = insertNode(a,15)
insertNode(a,5)
insertNode(a,8)
insertNode(a,3)
insertNode(a,13)
insertNode(a,16)
insertNode(a,14)


deleteNode(a,15)

