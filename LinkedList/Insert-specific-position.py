def InsertNth(head, data, position):
    new_node = Node(data) // this will create a new node
    if(position == 0):// if position is zero
        new_node.next = head; //new node next point to the current head
        return new_node
    else: 
        cnode = head  // temp varible node cnode = head
	/*
		iterate upto the givin position in linked list
                if position = 5
			then travel upto the position 4
	*/
        for i in range(position-1):
            cnode = cnode.next 
        /*
		new_node.next points to the current node next address
		crrent_node.next points to new_node
	*/
        new_node.next = cnode.next
        cnode.next = new_node
        return head
