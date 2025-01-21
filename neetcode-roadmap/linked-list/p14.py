def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    nodes = []
    current = head


    while current:
        nodes.append(current)
        current = current.next

    if len(nodes) - n == 0:
        return head.next
    
    first_node = nodes[len(nodes)-n-1]
    first_node.next = first_node.next.next

    return head