"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    queue = [root]
    temp = root
    op = ""
    while stack:
        temp = queue.pop(0)
        op += str(temp.data)+" "
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
    print(op)
