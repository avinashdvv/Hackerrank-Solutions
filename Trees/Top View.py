"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    if root == None:
        return
    queue = [[root,0]]
    dict = {}
    while queue:
        temp = queue.pop(0)
        tnode = temp[0]
        lvl = temp[1]
        if lvl not in dict:
            dict[lvl] = tnode.data
            print tnode.data,
        if tnode.left:
            queue.append([tnode.left,lvl-1])
        if tnode.right:
            queue.append([tnode.right,lvl+1])
        print(dict)
            
