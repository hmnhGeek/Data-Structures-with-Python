
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

    def length(self):
        # store the current head
        temp = self.head
        length = 0

        while temp.next != self.head:
            length += 1
            temp = temp.next

        length += 1 # for the last node.
        return length

    def value_at(self, index=0):
        temp = self.head # store the head somewhere.

        if index <= self.length() - 1:
            upcounter = 0
            while upcounter != index: # increase upcounter till you get to the correct node.
                upcounter += 1
                temp = temp.next

            return temp.data # return the data of the required node.
        return None

    def ascending(self, inherent_display=True):
        # this index will keep the ith minima
        i = 0

        while i != self.length()-1:
            # take the current ith position as minimum.
            m = self.value_at(i)
            m_index = i
            for j in range(i, self.length()):
                if self.value_at(j) < m: # loop each time to find the minimum starting from ith index and place that ith minimum at ith index.
                    m = self.value_at(j) # update the minimum
                    m_index = j

            # update i by increasing by 1.
            self.delete(m_index, False) # False so that it doesn't print the output.
            self.insert(m, i, False)
            i+=1

        if inherent_display:
            self.display()

    def previous_node(self, node_index=0):
        if node_index == 0:
            # traverse till the end.
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            return temp

        else:
            # traverse till that node.
            temp = self.head
            upcounter = 0
            while upcounter != node_index:
                upcounter += 1
                prev = temp
                temp = temp.next

            return prev

    def reverse(self, inherent_display=True):
        # take note of head.
        temp = self.head
        arr = [] # this array will be used to hold the self objects.

        while temp.next != self.head: # store each node in the array
            arr.append(temp)
            temp = temp.next

        # reverse the array.
        arr = arr[-1:-len(arr)-1:-1]

        # traverse till SECOND LAST node.
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]

        # for the last node, assign next to the first element of array arr (last element of the linked list).
        arr[i+1].next = arr[0]
        # assign the new head as the last element of the linked list.
        self.head = arr[0]

        if inherent_display:
            self.display()

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
    clist.insert(-1, 3)
    clist.insert(0)
    clist.insert(-9)
    clist.insert(100, 5)
    clist.delete()
    clist.delete()
    clist.delete(2)
    clist.find(2)
    print("Value at {} = {}".format(0, clist.value_at(0)))
    print("Sorted...")
    clist.ascending()
    pnode = clist.previous_node(2)
    print(pnode.data)
    clist.reverse()
