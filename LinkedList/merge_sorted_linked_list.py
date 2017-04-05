def MergeLists(nodeA, nodeB):
    mergedHead = Node()
    temp = mergedHead
    while nodeA != None or nodeB != None:
        if(nodeA == None):
            temp.next = nodeB
            break;
        elif(nodeB == None):
            temp.next = nodeA
            break;
        if(nodeA.data < nodeB.data):
            temp.next = nodeA
            nodeA = nodeA.next
            temp = temp.next
        else:
            temp.next = nodeB
            nodeB = nodeB.next
            temp = temp.next
    return mergedHead.next
            
