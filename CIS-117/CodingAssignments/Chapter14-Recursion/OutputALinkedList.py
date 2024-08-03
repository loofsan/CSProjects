class Node:
    def __init__(self, value):
        self.data_val = value
        self.next_node = None

    def insert_after(self, node):
        tmp_node = self.next_node
        self.next_node = node
        node.next_node = tmp_node

    def get_next(self):
        return self.next_node

    def print_data(self):
        print(self.data_val, end=", ")

# TODO: Write recursive print_list() function here.
def print_list(head):
    if head is None:
        # Base case: If head is None, we've reached the end of the list
        print(end=" ")
    else:
        if head.next_node is not None:
            print(f"{head.data_val}, ", end="")
        else:
            print(f"{head.data_val}", end=",")
        # Recursively print the rest of the list
        print_list(head.next_node)
       # Print current node's value

        
if __name__ == "__main__":
    size = int(input())
    value = int(input())
    head_node = Node(value) # Make head node as the first node
    last_node = head_node
    
    # Insert the second and the rest of the nodes
    for n in range(1, size):
        value = int(input())
        new_node = Node(value)
        last_node.insert_after(new_node)
        last_node = new_node
    
    print_list(head_node)