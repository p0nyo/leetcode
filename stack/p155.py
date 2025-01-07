class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = None
        self.dict = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if val in self.dict:
            self.dict[val] += 1
        else:
            self.dict[val] = 1
        if self.min == None:
            self.min = val
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
    
    def printDict(self):
        print(self.dict)
        


# Your MinStack object will be instantiated and called as such:
val = 1

obj = MinStack()
obj.push(val)
# obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)

obj.printDict()
