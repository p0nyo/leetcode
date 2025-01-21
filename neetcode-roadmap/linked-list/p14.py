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

# Trying O(1) space complexity
def removeNthFromEnd2(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    l = head
    r = head
    length = 0
    current = head

    while current:
        length += 1
        current = current.next

    if n == length:
        return head.next

    for _ in range(n+1):
        if r:
            r = r.next

    while r:
        l = l.next
        r = r.next

    l.next = l.next.next

    return head
    
    