def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    seen = set()
    current = head
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next

    return False