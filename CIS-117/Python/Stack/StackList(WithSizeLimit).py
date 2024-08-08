
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return f"\n".join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    # push
    def push(self):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append()
            return "The element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is no element to pop."
        else:
            self.list.pop()
            return "The element has been removed."

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is no element to pop."
        else:
            return self.list[len(self.list)-1]

    # delete 
    def delete(self):
        self.list = None

customStack = Stack(4)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)



