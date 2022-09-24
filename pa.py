class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        popped = self.stack.pop()
        return popped
    
    def length(self):
        return length(self.stack)
    
    def push(self,val):
        self.stack.append(val)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def print_stack(self):
        for ele in self.stack:
            print(ele, end = " ")
        print()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
s.print_stack()

        
