
class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return f"\n".join(values)
    
    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return "The value has been successfully inserted."

    # pop
    def pop(self):
        if self.list == []:
            return "There is no element in this stack"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.list == []:
            return self.list[len(self.list)-1]

    # delete
    def delete(self):
        self.list = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)