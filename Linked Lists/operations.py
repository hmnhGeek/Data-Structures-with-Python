# linked list implementation. # ref.: geeksforgeeks.org

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

    def insert(self, payload, index=0):
        # create a new node.
        tempNode = Node(payload)

        # we startoff with the very first node of the linked list as ``temp``.
        temp = self.head
        # node before the head node does not exist, so initialise it as None.
        prev = None

        # iterate till you reach the correct index.
        for i in range(index):
            # at each iteration, store the previous node and modify the ``temp``.
            prev = temp
            temp = temp.next
        
        if prev == None: # case when the insertion is at index = 0.
            # there exist no prev node. Just modify the tempNode as head.
            self.head = tempNode
            self.head.next = temp
        else:
            # when insertion is not to be done at 0, prev node pointer must be modified
            # so that it now points to tempNode.
            prev.next = tempNode
            tempNode.next = temp

    def delete(self, index=0):
        temp = self.head
        prev = None

        for i in range(index):
            prev = temp
            temp = temp.next
            
        # now temp is that node which we want to delete.
        if prev != None:
            tempNext = temp.next
            prev.next = tempNext
        else:
            # in case you want to delete 0th index, just modify the head.
            self.head = temp.next

        # free up temp
        temp = None

    def access(self, index=0):
        # setup the head.
        temp = self.head

        # iterate till you reach the correct index.
        for i in range(index):
            temp = temp.next

        return temp.data

    def length(self):
        # let the length be x.
        x = 0

        temp = self.head
        # iterate till temp.next = None
        while temp.next != None:
            x += 1
            temp = temp.next

        return x+1

    def search(self, item):
        # iterate till end and try to find the item.
        temp = self.head
        found_at = 0

        while temp.next != None:
            if temp.data == item:
                return found_at
            temp = temp.next
            found_at += 1

        # last check because if the item is on last node, the while loop will not run.
        if temp.data == item:
            return found_at
        else:
            # Not even on last node, its not present in the list.
            return "Not found"

    def reverse(self):
        # as always, start with head.
        temp = self.head
        # mmaintain a stack to store all the nodes.
        stack = []

        # start storing all the nodes.
        while temp.next != None:
            stack.append(temp)
            temp = temp.next

        # last node should be specially stored because while condition fails for it.
        stack.append(temp)

        # modify the head with original last node.
        self.head = stack[-1]

        # again start with a new head.
        temp = self.head

        # now the last node is on index 0 of the stack which used to be head but now isn't.
        # Therefore make this node's next attribute ``None``, else there will be a circular loop
        # between this and the stack[1] (second last element, now on).
        last_node = stack[0]
        last_node.next = None
        stack[0] = last_node

        # run in reverse direction of stack, remember LIFO.
        for i in range(-2, -len(stack)-1, -1):
            temp.next = stack[i] # this is like appending elements to new linked list.
            temp = stack[i] # as soon as this element is appended the last element is itself this element.
        
if __name__ == '__main__':
    # create a linked list l.
    l = LinkedList()

    d1 = Node(10)
    d2 = Node(13)
    d3 = Node(16)

    l.head = d1
    l.head.next = d2
    d2.next = d3

    # display the linked list.
    print("Before insertion...")
    l.printList()

    print("After insertion...")
    l.insert(-101, 0)
    l.insert(-90, 0)
    l.insert(67, 2)
    l.printList()

    print("Data at index 0...")
    print(l.access(0))

    print("Before deletion...")
    l.printList()

    print("After deletion...")
    l.delete(3)
    l.printList()

    print("Length of linked list...")
    print(l.length())

    print("Finding 10...")
    print(l.search(10))
    print("Finding 16...")
    print(l.search(16))
    print("Finding -101...")
    print(l.search(-101))

    print("Reversing...")
    l.printList()
    l.reverse()
    print("After reverse...")
    l.printList()
    
