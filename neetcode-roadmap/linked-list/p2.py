class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    carry = 0
    current1 = l1
    current2 = l2
    res = ListNode(0)

    def backtrack(head):
        if not current1 and not current2:
            return None
        
        if current1 == None:
            val1 = 0
        else:
            val1 = current1.val

        if current2 == None:
            val2 = 0
        else:
            val2 = current2.val

        val = val1 + val2 + carry
        carry = val % 10
        val = val - (carry * 10)

        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next

        new_node = ListNode(val)
        new_node.next = backtrack(new_node)
        
        return new_node
    
    res.next = backtrack(res)

    return res.next
        


