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
    return min.data

def searchMaximum(rootNode):
    max = rootNode
    if rootNode == None:
        return
    while max.right != None:
        max = max.right
    return max.data

def deleteNode(rootNode,item):
	temp = lookupTree(rootNode,item)
	#if rootnode is null return
	if rootNode == None:
		return
	#if the deleted node has no children make the parent pointer to non
	if temp.left is None and temp.right is None:
		temp.parent.left = None
		temp.parent.right = None
	#if the deleted node has one children make the parent pointer point to the children node
	#first we determine if temp is on left subtree or right subtree of the parent
	if temp.data < temp.parent.data: #left subtree
		if temp.left is not None and temp.right is None:
			temp.parent.left = temp.left
		if temp.left is None and temp.right is not None:
			temp.parent.left = temp.right
	if temp.data > temp.parent.data: #right subtree
		if temp.left is not None and temp.right is None:
			temp.parent.right = temp.left
		if temp.left is None and temp.right is not None:
			temp.parent.right = temp.right
	#if the deleted node has two children relabel the parent pointer with the first left node of the right node of the deleted node 

#must define rootNode first
a = node(10)
#automatically sort nodes after rootNode is inserted
insertNode(a,6)
insertNode(a,15)
insertNode(a,5)
insertNode(a,8)
insertNode(a,3)
insertNode(a,13)
insertNode(a,16)
insertNode(a,14)


deleteNode(a,10)

print(a.right.left.data)
