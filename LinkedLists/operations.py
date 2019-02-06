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
    

    def swap(self, index1, index2):

        if index1 != index2: 
            if index1 != 0 and index2 != 0: # this logic does not alter head.
                temp = self.head

                # find index 1..
                prev1 = None
                counter = 0
                while counter != index1 and temp.next != None:
                    counter += 1
                    prev1 = temp
                    temp = temp.next

                first_elem = temp # we have now found the first node.

                # finding index 2 now.
                prev2 = None
                temp = self.head
                counter = 0

                while counter != index2 and temp.next != None:
                    counter += 1
                    prev2 = temp
                    temp = temp.next

                second_elem = temp # this is the second node.

                # store the successor of the second node for a moment.
                next_of_sec_elem = second_elem.next

                prev1.next = second_elem # link the prev1 with the second node. But the second node still points to its successor.
                second_elem.next = first_elem.next # link the second node's pointer to the successor of first node. I this way, second node is now in correct place.
                prev2.next = first_elem # link the prev2 with first node. But the first node still points to its successor.
                first_elem.next = next_of_sec_elem # link the first node's pointer to the previous successor of second node which we deliberately stored. Now, even the first node is in place.

            else:
                if index1 == 0:
                    # in this case, we only need to find the second node, because node is the head itself.
                    temp = self.head
                    counter = 0
                    prev2 = None

                    # find the second node.
                    while counter != index2 and temp.next != None:
                        counter += 1
                        prev2 = temp
                        temp = temp.next

                    # temp is now the second node.

                    prevHead = self.head # store the current head for a while.
                    next_ofprevHead = prevHead.next # store the successor of current head, that is the first element.
                    prev2.next = prevHead # link the current head as successor of "precursor of temp which is the second node".
                    prevHead.next = temp.next # link the current head's pointer to second node's successor, in this way, the current head has been moved to a new position.
                    temp.next = next_ofprevHead # modify the second node's pointer to successor of previous Head, because it still references the original successor. That is, now link it to first element of the linked list.
                    self.head = temp # make the second node as new head.

                elif index2 == 0:
                    # repeat the above logic if index2 is 0.
                    temp = self.head
                    counter = 0
                    prev1 = None
                    while counter != index1 and temp.next != None:
                        counter += 1
                        prev1 = temp
                        temp = temp.next

                    prevHead = self.head
                    next_ofprevHead = prevHead.next
                    prev1.next = prevHead
                    prevHead.next = temp.next
                    temp.next = next_ofprevHead
                    self.head = temp

    def pairwiseSwap(self):
        # store the head.
        temp = self.head

        # get the length of the linked list.
        linear_wt = self.length()

        # find the number of pairs
        pairs = int(linear_wt/2)
        upcounter = 0
        prev = None
        print("Pairs = {}".format(pairs))

        while upcounter <= pairs:
            first_node = temp
            temp = temp.next
            second_node = temp

            # save the second_node pointer
            secPointer = second_node.next
            # link first node with secPointer
            first_node.next = secPointer
            # link second node to first node
            second_node.next = first_node

            # change the temp to the first node of next pair.
            temp = first_node.next

            # if the swap is hapenning on first two nodes, then assign the second node (index = 1) as head node.
            if upcounter == 0:
                self.head = second_node
            # else, connect the previous node of current first node to the current second node.
            else:
                prev.next = second_node

            # update upcounter by +2, so that we move in pairs.
            upcounter += 2
            # don't forget to assign a previous node. Now the first node has actually become the second node.
            # prev is needed as 1 for example in this case, 2 ----> 1 ----> 3 <---- 4. So that this prev (1), can be linked to 4 and thus making this,
            # 2 ----> 1 ----> 4 ----> 3.
            prev = first_node
        
        
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

    print("Before swapping...")
    l.printList()
    print("After swapping...")
    l.swap(2, 0)
    l.printList()

    print("Before pairwise swap...")
    l.printList()
    print("After pairwise swap...")
    l.pairwiseSwap()
    l.printList()
    
