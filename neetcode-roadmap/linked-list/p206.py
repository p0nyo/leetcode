
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"current: {self.val}, next value: {self.next.val}"

def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """ 
    prev, current = None, head

    while current != None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    return prev



l3 = ListNode(3, None)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

# 1 -> 2 -> 3 -> None

print(reverseList(l1))

