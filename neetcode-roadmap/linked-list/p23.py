def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    # 1 -> 2 -> 3
    # 2 -> 3 -> 4

    if not list1:
        return list2
    elif not list2:
        return list1

    if list1.val <= list2.val:
        res, current, other = list1, list1, list2
    else:
        res, current, other = list2, list2, list1

    while current.next:
        if current.next.val >= other.val:
            temp = current.next
            current.next = other
            other = temp
        current = current.next
    if other:
        current.next = other
    return res

def mergeKLists(lists):
    """
    :type lists: List[Optional[ListNode]]
    :rtype: Optional[ListNode]
    """
    if len(lists) < 2:
        return None

    res = mergeTwoLists(lists[0], lists[1])

    for i in range(2, len(lists)-1):
        res = mergeTwoLists(res, list[i+1])

    return res