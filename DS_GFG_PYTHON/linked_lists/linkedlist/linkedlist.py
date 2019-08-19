# This is the code for linked lists

# define a node class
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# define a linked list class
class LinkedList():
    def __init__(self):
        self.head = None

    def length(self):
        '''
        Returns the length of the linked list.
        '''
        if self.head == None:
            return 0
        else:
            last = self.head
            count = 1

            while last.next != None:
                last = last.next
                count += 1

            return count

    def append(self, data):
        '''
        Adds an element to the end of the linked list.
        '''
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
        else:
            last = self.head

            while last.next != None:
                last = last.next

            last.next = newnode

    def display(self):
        '''
        Prints the linked list.
        '''
        if self.head == None:
            print(" ")

        else:
            last = self.head

            while last.next != None:
                print(last.data, end=" ---> ")
                last = last.next

            print(last.data)
            

    def reverse(self):
        '''
        Reverses the linked list.
        '''
        if self.head == None:
            return "Empty list!"
        else:
            last = self.head
            prev = None

            while last != None:
                Next = last.next
                last.next = prev
                prev = last
                last = Next

            self.head = prev

    def loc(self, item):
        '''
        Returns the index of the item in the linked list.
        '''
        last = self.head
        counter = 0

        while last != None and last.data != item:
            last = last.next
            counter += 1
        return counter

    def ret_val(self, index):
        '''
        Returns the value at index.
        '''
        if index in range(0, self.length()):
            count = 0
            last = self.head

            while count != index:
                last = last.next
                count += 1

            return last.data
        else:
            return "Out of bounds!"

    def remove_first(self):
        '''
        Removes the first element.
        '''
        if self.head == None:
            return "Can't delete further!"
        else:
            current_head = self.head
            self.head = self.head.next

            del current_head

    def remove_last(self):
        '''
        Removes the last element.
        '''
        if self.length() == 0:
            return "Can't delete further!"
        elif self.length() == 1:
            current_head = self.head
            self.head = None
            del current_head
        else:
            last = self.head

            while last.next != None:
                prev = last
                last = last.next

            prev.next = None
            del last

    def delete(self, index):
        '''
        General method to delete any element in the linked list.
        '''
        if index == 0:
            self.remove_first()
        elif index == self.length() - 1:
            self.remove_last()
        elif index in range(1, self.length()-1):
            current = self.head
            prev = None
            count = 0
            
            while count != index:
                count += 1
                prev = current
                current = current.next
                
            prev.next = current.next
            del current

    def ispallindrome(self):
        '''
        Returns true if the linked list is pallindrome.
        '''
        current = self.head
        string = ''

        while current != None:
            string += str(current.data)
            current = current.next

        return Utility().checkpallindrome(string)

    def remove_duplicates(self):
        '''
        Removes the duplicate items from the linked list. Takes single values.
        '''
        if self.length() >= 1:
            current = self.head
            prev = self.head

            while current != None:

                if prev.data == current.data:
                    # if the data on both current and prev is same, modify the perv's next to curr next.
                    prev.next = current.next
                    temp = current
                    current = current.next
                    del temp
                else:
                    # we must have removed the duplicates, update to new prev.
                    prev = current
                    current = current.next

    def swap(self, index1, index2):
        '''
        Swaps two elements in the linked list.
        '''
        length = self.length()
        
        if index1 in range(length) and index2 in range(length):

            i1 = min(index1, index2)
            i2 = max(index1, index2)

            # making index 1 as first node to encounter and node 2 as second, this makes processing easier.
            index1 = i1
            index2 = i2

            count1, count2 = 0, 0
            current = self.head
            prev1, prev2 = None, None

            # reach to the first node
            while count1 != index1:
                prev1 = current
                current = current.next
                count1 += 1
            next1 = current.next
            node1 = current

            current = self.head

            # reach the second node
            while count2 != index2:
                prev2 = current
                current = current.next
                count2 += 1
            next2 = current.next
            node2 = current

            if abs(index2 - index1) != 1:
                node1.next = next2
                node2.next = next1

                if prev1 != None: # this means node 1 is head.
                    prev1.next = node2
                else:
                    self.head = node2
                prev2.next = node1
            
            else:
                # if the nodes are adjacent
                node1.next = node2.next
                if prev1 != None: # this means node 1 is head.
                    prev1.next = node2
                else:
                    self.head = node2
                node2.next = node1

    def pairwise_swap(self):
        i = 0
        while i <= self.length()-1:
            i1, i2 = i, i+1
            self.swap(i1, i2)
            i = i+2

    def ispresent(self, item):
        if self.loc(item) == self.length():
            return False
        else:
            return True

    def find_min(self):
        '''
        Returns the minimum element of the linked list.
        '''
        least = float("inf")

        current = self.head
        while current != None:
            if current.data < least:
                least = current.data
            current = current.next

        return least, self.loc(least)

    def slice_out(self, start, stop):
        '''
        Returns the slice of a linked list. Stop is not included.
        '''
        length = self.length()
        
        if start <= stop and start in range(length) and stop in range(length+1):
            count = 0

            current = self.head
            while count < stop:
                if count >= start:
                    if count != stop -1:
                        print(current.data, end=" ---> ")
                    else:
                        print(current.data)
                count += 1
                current = current.next

    def bubble_sort(self):
        '''
        Bubble sort to sort out the linked list. Note that the sorting changes the original list.
        '''
        swapped_once = True

        while swapped_once:
            swapped_once = False
            
            for i in range(self.length()-1):
                val1 = self.ret_val(i)
                val2 = self.ret_val(i+1)

                if val1 > val2:
                    self.swap(i, i+1)
                    swapped_once = True
                
class Utility():
    def __init__(self):
        pass

    def checkpallindrome(self, string):
        n = len(string)

        if n % 2 == 0:
            if string[0:int(n/2)] == string[-1: -int(n/2) - 1:-1]:
                return True
            else:
                return False
        else:
            if string[0:int((n-1)/2)] == string[-1: -int((n-1)/2) - 1: -1]:
                return True
            else:
                return False

    def linkedlist_intersection(self, l1, l2):
        current = l1.head
        resultll = LinkedList()

        while current != None:
            if l2.ispresent(current.data): # check if the element of l1 is in l2 or not.
                resultll.append(current.data)
            current = current.next
        return resultll

def driver():
    l = LinkedList()
    l.append(1)
    l.append(1)
    l.append(1)
    l.append(2)
    l.append(2)
    l.append(3)
    l.append(3)
    l.append(3)
    l.append(3)
    l.append(-1)
    l.display()
    l.swap(8, 9)
    l.display()
    l.swap(0, 1)
    l.display()
    l.pairwise_swap()
    l.display()
    l.bubble_sort()
    l.display()
##    l.slice_out(6, l.length())
##    for i in range(11):
##        l.append(i)
##    l.display()
##    l.pairwise_swap()
##    l.display()
##    print(l.ispresent(100))
