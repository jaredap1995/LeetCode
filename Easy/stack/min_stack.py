"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function."""

class MinStack_O_n(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, val):
        self.stack.append(val)
        return self.stack

        
    def pop(self):
        self.stack.pop()
        return self.stack


    def top(self):
        return self.stack[-1]


    def getMin(self):
        min=self.stack[0]
        for i in self.stack:
            if i<min:
                min=i
        return min
        

class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <=self.min_stack[-1]:
            self.min_stack.append(val)

        
    def pop(self):
        val=self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# BEGIN: ed8c6549bwf9
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin()) # Output: -3
obj.pop()
print(obj.top()) # Output: 0
print(obj.getMin()) # Output: -2
# END: ed8c6549bwf9
print(obj)