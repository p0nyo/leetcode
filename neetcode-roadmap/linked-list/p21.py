class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    # 1 -> 2 -> 3
    # 2 -> 3 -> 4

    if list1.val <= list2.val:
        res, current, other = list1, list1, list2
    else:
        res, current, other = list2, list2, list1

    while current:
        if current.next >= other.val:
            temp = current.next
            current.next = other
            other = temp
            current = current.next
    return res




    

    
