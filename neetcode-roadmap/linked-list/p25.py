def reverseKGroup(head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """

    # loop thru the linked list and when counter == k, reset
    counter = 1
    res_list = []
    temp_list = []
    current = head

    while current:
        if counter > k:
            temp_list.reverse()
            res_list += temp_list
            counter = 1
            temp_list = []
        temp_list.append(current)
        counter += 1
        current = current.next
    res_list += temp_list

    res_list[-1].next = None
    for i in range(len(res_list)-2,-1,-1):
        res_list[i].next = res_list[i+1]
        
    return res_list[0]


    
