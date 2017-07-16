"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
stack = []
def inOrder(root):
    temp = root
    op = ""
    while 1:    
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            if len(stack) == 0:
                break
            temp = stack.pop()
            op += str(temp.data)+" "
            temp = temp.right
        
    print(op)
----------------------------------
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
op = ""
def tinOrder(root):
    global op
    if root:
        tinOrder(root.left)
        op += str(root.data)+" "
        tinOrder(root.right)
def inOrder(root):
    global op
    tinOrder(root)
    print(op)
    
            
            
