class node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

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

#must define rootNode first
a = node(3)
#automatically sort nodes after rootNode is inserted
insertNode(a,2)
