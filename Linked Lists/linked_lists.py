# linked list implementation. # ref.: geeksforgeeks

class Node:
    # a node contains data and a pointer to next node.
    # a node is always assigned a blank pointer first.
    # a node is thus a general entity.
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # a linked list on the other hand consists of several nodes.
    # we need a linked list class so that we can assign a particular Node()
    # class as head and so that different nodes can be connected together
    # as one data structure.

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

def node_array(head_node):
    curr_node = head_node

    traversing = True
    last_loop = False
    
    while traversing:
        print(curr_node.data)

        if not last_loop:
            curr_node = curr_node.next
            if curr_node.next == None:
                last_loop = True
        else:
            break

if __name__ == '__main__':
    lnklist = LinkedList()
    lnklist.head = Node(1)
    second = Node(6)
    third = Node(3)

    lnklist.head.next = second
    second.next = third

    lnklist.printList()

    # lets see whats the problem if we only use Node() to make a linked list.
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n3 = Node(3)
    n2.next = n3

    # in this case, if we have to print the list.
    curr_node = n1
    traversing = True
    last_loop = False
    
    while traversing:
        print(curr_node.data)

        if not last_loop:
            curr_node = curr_node.next
            if curr_node.next == None:
                last_loop = True
        else:
            break

    # creating a snippet again and again would be cumbersome.
    # What we can do is that we create a global function for this.
    # it has been done above.
    node_array(n1)

    # creating a global function does not make the code efficient in the way of OOPs.
    # That's why creating a separate class for linked list is efficient.
