
op = ""
def tpostOrder(root):
    global op
    if root:
        tpostOrder(root.left)
        tpostOrder(root.right)
        op += str(root.data)+" "
        
def postOrder(root):
    global op
    tpostOrder(root)
    print(op)
    
-----------------------------
