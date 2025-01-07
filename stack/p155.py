class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = [None]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.min_stack) != 0:
            if self.min_stack[-1] == None:
                self.min_stack.append(val)
            elif val <= self.min_stack[-1]:
                self.min_stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if len(self.min_stack) != 0:
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:


# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)

# print(minStack.stack)
# print(minStack.min_stack)

# print(minStack.getMin())
# minStack.pop()
# print(minStack.top())
# print(minStack.getMin())


obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.stack)
print(obj.min_stack)
print(obj.getMin())
obj.pop()
print(obj.getMin())
