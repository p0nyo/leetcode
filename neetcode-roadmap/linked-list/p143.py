def reorderList(head):
    """
    :type head: Optional[ListNode]
    :rtype: None Do not return anything, modify head in-place instead.
    """
    nodes = []
    current = head

    while current:
        nodes.append(current)
        current = current.next

    i, j = 0, len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i >= j:
            break
        nodes[j].next = nodes[i]
        j -= 1
    nodes[i].next = None
