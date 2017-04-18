"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    currA = headA
    currB = headB
    la = 0
    lb = 0
    while(currA != None):
        currA = currA.next
        la += 1
    while(currB != None):
        currB = currB.next
        lb += 1
    diff = abs(la-lb)
    if(la<lb):
        slow = headA
        fast = headB
        for i in range(diff):
            fast = fast.next
        while(slow.data != fast.data):
            slow = slow.next
            fast = fast.next
        return slow.data
    else:
        slow = headB
        fast = headA
        for i in range(diff):
            fast = fast.next
        while(slow.data != fast.data):
            slow = slow.next
            fast = fast.next
        return slow.data
