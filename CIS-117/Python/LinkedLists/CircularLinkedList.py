

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Creation of Circular Singly Linked List
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return("The CSLL has been created.")

    # Insertion of CSLL
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head 
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next 
                self.tail.next = newNode
                self.tail = newNode 
            else:
                tempNode = self.head 
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return("The node has been successfully inserted.")

    #Traversal of a node in CSLL
    def traversalCSLL(self):
        if self.head is None:
            print("There is no linked list.")
        
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    
    # Delete a CSLL
    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in CSLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail = self.head

            if location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


CSLL = CSLinkedList()
CSLL.createCSLL(0)
CSLL.insertCSLL(2, 1)
CSLL.insertCSLL(3, 1)
CSLL.insertCSLL(4, 1)
CSLL.insertCSLL(5, 1)
print([node.value for node in CSLL])
CSLL.traversalCSLL()
CSLL.deleteNode(3)
print([node.value for node in CSLL])