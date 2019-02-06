
class Node(object):

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL(object):
    def __init__(self):
        self.head = None

    def display(self, direction=0):

        if direction == 0:
            # note down the head.
            temp = self.head

            while temp.next != None:
                print(temp.data)
                temp = temp.next

            print(temp.data)
        else:
            # go to the last node
            temp = self.head

            while temp.next != None:
                temp = temp.next

            # print in reverse direction
            while temp.prev != None:
                print(temp.data)
                temp = temp.prev
            print(temp.data)

    def insert(self, item, index=0):
        # take care of the head.
        temp = self.head
        if index == 0:
            new_node = Node(item) # create the new node.
            self.head.prev = new_node # current head's previous
            new_node.next = self.head # new node follower

            self.head = new_node # now the new node is the head

        else:
            new_node = Node(item)
            upcounter = 0

            while upcounter != index-1: # traverse to the index just before the required index.
                upcounter += 1
                temp = temp.next


            # Previously, temp <---> nextnode
            # now, temp <---> new_node <---> next_node
            try:
                nextnode = temp.next
                temp.next = new_node
                new_node.next = nextnode
                new_node.prev = temp
                nextnode.prev = new_node
            except:
                pass

    def delete(self, index=0):
        # take care of the head.
        temp = self.head
        copy = self.head

        if index == 0:
            self.head = temp.next
            self.head.prev = None
            copy = None

        else:
            # go to that index
            upcounter = 0
            while upcounter != index:
                upcounter += 1
                temp = temp.next

            previous = temp.prev
            Next = temp.next

            previous.next = Next
            try:
                Next.prev = previous
            except AttributeError:
                print("You must be deleting the last index. An error occured but it should not be a concern to you. However, the element has been deleted.")

            del temp

    def reverse(self):
        # take note of the head.
        temp = self.head

        while temp.next != None:
            temp = temp.next

        # modify head with temp (the last node).
        self.head = temp

        #          <---   <---   <---   
        # X <--- 1 ---> 2 ---> 3 ---> 4 ---> X
        #
        
        while temp.prev != None: # traverse until you reach 1.
            # while traversing, do this.

            nodenext = temp.next # store the next part of current node. Because later, the next will become the previous.
            temp.next = temp.prev # change next to previous. Now both next and previous point to same node.
            temp.prev = nodenext # therefore, change previous to original next which we stored above.
            temp = temp.next # although we need to go to previous node, but now the previous node is next node. Hence, go to the next node.

        if temp.prev == None: # last node is a special case because while will not entertain this.
            temp.prev = temp.next # change its previous to next.
            temp.next = None # make the next as None.

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    dll = DLL()
    dll.head = n1
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3

