"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def RemoveDuplicates(head):
    curr = head;
    dict = {}
    while(curr.next != None):
        dict[curr.data] = curr.data
        if(curr.next.data in dict):
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
            