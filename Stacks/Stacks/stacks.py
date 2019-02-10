
import sys
sys.path.append('LinkedLists')

# import linked lists. we will use them to implement stacks.
from LinkedLists import linked_lists

class Stack(object):

    ''' Stack implementation. Stack is LIFO or FILO. '''

    def __init__(self):
        self.stack = linked_lists.LinkedList()

    def isempty(self):
        ''' Returns True if stack is empty. '''
        if self.stack.head == None:
            return True
        else:
            return False

    def push(self, item):
        # let stack be s = [1,2,3,4]. Stack length is 4. Hence, insert item at stack length, which is 4, i.e. last position.
        self.stack.insert(item, self.stack.length())

    def pop(self):
        # check if stack is empty or not.
        if self.isempty():
            return "Stack is empty."
        else:
            # let stack be s = [1,2,3,4]. Stack length -1 = 3. Delete last element which is at 3 and return it.
            retval = self.stack.access(self.stack.length()-1)
            self.stack.delete(self.stack.length()-1)
            return retval

    def top(self):
        if self.isempty():
            return None
        return self.stack.access(self.stack.length()-1)

    def display(self):
        self.stack.printList()

    def ismember(self, item):
        if self.stack.search(item) != "Not found":
            return True
        else:
            return False
