

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List

    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created successfully."

    # Insertion Of DLL
    
    def insertDLL(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted.")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
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

    # Traverse through doubly linked list
    def traversalDLL(self):
        if self.head is None:
            print("There is no element to traverse.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse traversal through doubly linked list

    def reversetraversal(self):
        if self.head is None:
            print("There is no element to traverse")
        
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search for an element in Doubly lInked lIst

    def searchDLL(self, nodeValue):
        if self.head is None:
            print("There is no element to search.")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list."

    # Deleting a doubly linked list

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
                    self.head.prev = None

            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                    curNode.next = curNode.next.next
                    curNode.next.prev = curNode
                print("The node has been successfully deleted.")

    # Deleting an Entire DLL

    def deleteDLL(self):
        if self.head is None:
            print('There is no nodes in the DLL.')
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted.")


doublyLL = DoublyLL()
doublyLL.createDLL(5)
doublyLL.insertDLL(0, 0)
doublyLL.insertDLL(2, 1)
doublyLL.insertDLL(3, 1)
doublyLL.insertDLL(4, 2)
print([node.value for node in doublyLL])
