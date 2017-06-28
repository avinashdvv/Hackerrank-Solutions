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

def preOrder(root):
    if root != None:
        print(str(root.data)+' ')
        preOrder(root.left)
        preOrder(root.right)
    
