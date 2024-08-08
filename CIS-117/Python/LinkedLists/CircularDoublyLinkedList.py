
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    # Creation of CDLL
     
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully."

    # Insertion of CDLL
    def insertDLL(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted.")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = self.head
                newNode.next = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode  

    # Traversal of CDLL
    def traversal(self):
        if self.head is None:
            print("There is no node to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Deletion of Node
    def deleteNode(self, location):
        if self.head is None:
            print('There is no element to delete.')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head 

            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
                print("The node has been successfully deleted.")

    # Delete an entire CDLL
    def deleteCDLL(self):
        if self.head is None:
            print("There is no element to delete.")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next 
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted.")


circularDLL = CircularDLL()
circularDLL.createCDLL(2)
print([node.value for node in circularDLL])