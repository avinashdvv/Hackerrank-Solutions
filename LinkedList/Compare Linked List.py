"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    curr1 = headA
    curr2 = headB
    c1 = 0
    c2 = 0
    while(curr1.next != None):
        curr1 = curr1.next
        c1 += 1
    while(curr2.next != None):
        curr2 = curr2.next
        c2 += 1
    if(c1 == c2):
        curr1 = headA
        curr2 = headB
        status = None;
        while(curr1.next != None):
            curr1 = curr1.next
            curr2 = curr2.next
            if(curr1.data == curr2.data):
                status = True
            else:
                status = False
                break
        if(status == True):
            return 1
        else:
            return 0
    else:
        return 0
