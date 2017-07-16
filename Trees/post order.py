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

def postOrder(root):
    op = ""
    curr = root 
    stack = []
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if temp == None:
                temp = stack.pop()
                op += str(temp.data)+" "
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    op += str(temp.data)+" "
            else:
                curr = temp
    print(op)
---------------------------------------

def postOrder(root):
    op = ""
    temp = root 
    stack = []
    s2 = []
    stack.append(temp)
    while stack:
        temp = stack.pop()
        s2.append(temp)
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)
    for i in range(len(s2)-1,-1,-1):
        op += str(s2[i].data)+" "
    print(op)
        
