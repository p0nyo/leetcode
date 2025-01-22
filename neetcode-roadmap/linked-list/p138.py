
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random



def copyRandomList(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    dictmap = {}

    def backtrack(node):
        if node == None:
            return None
        # if node in dictmap:
        #     return dictmap[node]

        new_node = Node(node.val)
        dictmap[node] = new_node
        new_node.next = backtrack(node.next)
        new_node.random = dictmap.get(node.random)

        return new_node

    return backtrack(head)
