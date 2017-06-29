"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
# using stack
def preOrder(root):
    op = ""
    stack = []
    stack.append(root)
    while stack:
        temp = stack.pop()
        op += str(temp.data)+" "
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)
    print(op[:-1])
#-------------------------------
op = ""
def tpreOrder(root):
    global op
    if root != None:
        op += str(root.data)+" "
        tpreOrder(root.left)
        tpreOrder(root.right)
def preOrder(root):
    tpreOrder(root)
    print(op)    
