"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    fast = head.next;
    slow = head;
    status = None
    if(head == None):
        return False
    while(fast != None and fast.next != None and slow != None):
        if(fast == slow):
            return True
        fast = fast.next.next
        slow = slow.next
    return False
