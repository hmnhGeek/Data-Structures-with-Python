class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def length(self):
        if self.head == None:
            return 0
        else:
            count = 1
            current = self.head

            while current.next != self.head:
                count += 1
                current = current.next
            return count

    def append(self, data):
        ''' Returns the new linked list with data appended. '''
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.head.prev = self.head
            self.head.next = self.head
        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = newnode
            newnode.prev = current
            newnode.next = self.head
            self.head.prev = newnode

    def insert(self, index, value):
        '''Inserts a node at index = index.'''
        index %= self.length()
        
        if index == self.length():
            self.append(value)
        else:
            if index == 0:
                last_node = self.get_node(self.length()-1)
                newnode = Node(value)

                head = last_node.next
                last_node.next = newnode
                newnode.prev = last_node
                head.prev = newnode
                newnode.next = head

                self.head = newnode

            else:
                newnode = Node(value)

                current = self.head
                count = 1
                
                while count != index:
                    current = current.next
                    count += 1

                oldnext = current.next
                current.next = newnode
                newnode.prev = current
                newnode.next = oldnext
                oldnext.prev = newnode
    
    def display(self):
        '''Prints the linked list.'''
        if self.head == None:
            return "Empty linked list."
        else:
            current = self.head

            while current.next != self.head:
                print(current.data, end=" <---> ")
                current = current.next

            print(current.data)


    def get_node(self, index):
        '''Returns the Node object at index = index.'''
        if index == 0:
            return self.head
        else:
            current = self.head
            count = 0
            index = index % self.length()

            while count != index:
                current = current.next
                count += 1
            
            return current

    def swap(self, index1, index2):
        '''Swaps nodes at index1 and index2.'''
        index1, index2 = index1 % self.length(), index2 % self.length() # to protect from leap bounds.

        i1 = min(index1, index2)
        i2 = max(index1, index2)

        index1, index2 = i1, i2

        if i1 == 0 and i2 == self.length()-1:
            # get the first node.
            n1 = self.get_node(i1)
            # get the second node.
            n2 = self.get_node(i2)

            p1, p2 = n1.next, n2.prev

            n2.next = n1.next
            n2.prev = n1
            n1.next = n2
            p1.prev = n2
            p2.next = n1

            self.head = n2
            
        elif abs(i1-i2) != 1: # nodes are not adjacent
            # get the first node.
            n1 = self.get_node(i1)
            # get the second node.
            n2 = self.get_node(i2)

            # check if n1 is head
            head = False
            if self.head == n1:
                head = True

            prime_prev, prime_next = n1.prev, n1.next
            node2_prev, node2_next = n2.prev, n2.next
            
            n1.next = n2.next
            n1.prev = n2.prev
            
            n2.next = prime_next
            n2.prev = prime_prev
            
            prime_next.prev = n2
            prime_prev.next = n2
            node2_prev.next = n1
            node2_next.prev = n1

            if head:
                self.head = n2

        else:

            # get the first node.
            n1 = self.get_node(i1)
            # get the second node.
            n2 = self.get_node(i2)
            p, q = n1.prev, n2.next

            head = False
            if n1 == self.head:
                head = True
            
            n1.next = n2.next
            n1.prev = n2
            n2.next = n1
            n2.prev = p
            p.next = n2
            q.prev = n1

            if head:
                self.head = n2

    def pairwise_swap(self):
        i = 0

        while i < self.length():
            self.swap(i, i+1)
            i += 2

    def bubble_sort(self):
        '''Sorts the linked list.'''
        swapped_once = True

        while swapped_once:
            swapped_once = False
            count = 0
            current = self.head
            
            while count != self.length() - 1:
                if current.data > current.next.data:
                    self.swap(count, count + 1)
                    swapped_once = True
                count += 1
                current = current.next

    def delete(self, index):
        '''Deletes the node at index = index.'''
        index %= self.length()
        
        if index == 0:
            temp = self.head
            head_next = self.head.next
            head_prev = self.head.prev

            head_prev.next = head_next
            head_next.prev = head_prev

            self.head = head_next
            del temp

        else:
            current = self.head
            count = 0

            while count != index:
                current = current.next
                count += 1

            temp = current
            curr_prev = temp.prev
            curr_next = temp.next
            curr_prev.next = curr_next
            curr_next.prev = curr_prev

            del temp

    def print_reverse(self):
        ''' Prints the linked list in reverse. Original list remains the same.'''
        current = self.head.prev

        while current != self.head:
            print(current.data, end=" <--->")
            current = current.prev
        print(current.data)

    def get_index(self, node):
        ''' Returns the index of the node datatype in the linked list. '''
        count = 0
        current = self.head

        while current != node and current.next != self.head:
            count += 1
            current = current.next

        if count < self.length():
            return count
        else:
            return -1

    def delete_value(self, item):
        ''' Deletes the first occurance of the item in the linked list. '''
        current = self.head
        count = 0

        while count != self.length():
            if current.data == item:
                self.delete(count)
                break
            count += 1
            current = current.next

    def ismember(self, item):
        ''' Checks whether an item is in the list. '''
        current = self.head
        count = 0

        while count != self.length():
            if current.data == item:
                return True
            count += 1
            current = current.next
        return False

    def count(self, item):
        ''' Returns the count of the item in the linked list. '''
        current = self.head
        count = 0
        val = 0

        while count != self.length():
            if current.data == item:
                val += 1
            count += 1
            current = current.next
        return val

        
class Utility():
    def __init__(self):
        pass
    def split(self, index, circ_linked_list):
        if index == 0:
            return
        else:
            index = index % circ_linked_list.length()
            
            current = circ_linked_list.head
            count = 0

            while count != index:
                current = current.next
                count += 1

            # we are now on the new head
            newhead = current

            while current.next != circ_linked_list.head:
                current = current.next

            old_previous = newhead.prev
            newhead.prev = current
            current.next = newhead

            newList = DoublyLinkedList()
            newList.head = newhead

            old_previous.next = circ_linked_list.head
            circ_linked_list.head.prev = old_previous

            return circ_linked_list, newList

    def remove_duplicates(self, linked_list):
        reference = DoublyLinkedList()

        current = linked_list.head

        while current.next != linked_list.head:

            if not reference.ismember(current.data):
                reference.append(current.data)

                while linked_list.count(current.data) != 1:
                    linked_list.delete_value(current.data)
                current = current.next
            else:
                current = current.next
        return linked_list, reference
            

def driver():
    import random
    l = DoublyLinkedList()
    for i in range(50):
        l.append(random.randint(0, 10))

    l.display()
    l, r = Utility().remove_duplicates(l)
    l.display()
    l.bubble_sort()
    l.display()
    
driver()
    
