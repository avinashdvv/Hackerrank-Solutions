def Delete(head, position):
    current = head // temparary varible to the head
    if (position == 0): //if first need to be removed making the next node as a head node
        head = head.next
        return head
    else:
	/*
		itarate upto position-1 the positon and update the current node 
		and make current_node.next = current_node of next of next
		here we are updating the current_node next address to next of next node
	*/
        for i in range(position-1):
            current = current.next
        current.next = current.next.next
        return head
  
  
  

