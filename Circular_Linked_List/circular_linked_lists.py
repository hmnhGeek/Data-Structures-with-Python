
class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

class circular():
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head

        while temp.next != self.head: # since last node's next points to head node.
            print(temp.data)
            temp = temp.next

        print(temp.data) # last node will not be counted in the while loop. Print it explicitly.

    def insert(self, item, index=0, inherit_display=True):
        # check if the index is 0. Because then, the head needs to be modified.
        if index == 0:
            # store the current head.
            temp = self.head
            dummy = self.head
            # create a new node.
            self.head = Node(item)
            self.head.next = temp

            # now the last node has to point to this new head.
            # find it using O(n) linear traversal.
            while dummy.next != temp:
                dummy = dummy.next

            # we are now on the last node.
            # modify it.
            dummy.next = self.head

        else:
            # store the head
            temp = self.head
            upcounter = 0

            while upcounter != index:
                prev = temp
                temp = temp.next
                upcounter += 1

            # now we are at the correct index.
            # make prev point to new node.
            new_node = Node(item)
            prev.next = new_node
            new_node.next = temp
        
        if inherit_display:
            print('==============')    
            self.display()

    def delete(self, index=0, inherent_display=True):
        # if the index is 0, create a new head.
        if index == 0:
            # store the current head.
            temp = self.head
            curr_head = self.head

            # traverse to the last node in O(n)
            while temp.next != curr_head:
                temp = temp.next

            # we are now with temp as last node.
            # change temp's next to new head.
            temp.next = curr_head.next
            self.head = curr_head.next

            # free up the memory
            curr_head = None

        else:
            # if index is not 0.
            temp = self.head
            upcounter = 0

            # traverse till that node.
            while upcounter != index:
                prev = temp
                temp = temp.next
                upcounter += 1

            # this brings us to the correct index.
            prev.next = temp.next
            # free up temp
            temp = None

        if inherent_display:
            print('=============')
            self.display()

    def find(self, value):
        # store the head.
        temp = self.head
        curr_head = self.head
        index = 0

        # traverse and find
        while temp.next != curr_head:
            if temp.data == value:
                print("Found at {}".format(index))
                break
            else:
                temp = temp.next
                index += 1
        else:
            if temp.data == value:
                print("Found at {}".format(index))
            else:
                print("Not found")

if __name__ == '__main__':
    print("Welcome to circular linked lists ...")
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    clist = circular()
    clist.head = n1
    clist.head.next = n2
    n2.next = n3
    n3.next = clist.head

    clist.display()
    clist.insert(0)
    clist.insert(4, 4)
    clist.insert(5, 2)
    clist.delete()
    clist.delete()
    clist.delete(2)
    clist.find(2)
